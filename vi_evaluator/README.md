# Vietnamese evaluator — triển khai nhiệm vụ của Huy

**Bộ dữ liệu gồm 1.050 câu đã được nhóm review**

Đây là model chấm chất lượng câu tiếng Việt mới, tách biệt với model ViSP sinh câu đã fine-tune trước đó. Encoder và các head đều được cập nhật trọng số. JFLEG và SEEDA là tài liệu thiết kế đánh giá; dự án này không phát hành lại hai bộ benchmark chính thức dưới tên tiếng Việt.

## Dữ liệu thực tế

| Nguồn | Train | Validation/dev | Test |
|---|---:|---:|---:|
| ViSP tải từ revision đã khóa | 406.308 | 391.044 | 380.590 |
| ViSP sau kiểm tra nhóm giao nhau và cặp trùng | 365.311 | 306.831 | 376.060 |
| Dữ liệu nhóm đủ điều kiện | 697 | 141 | 150 |

Tổng ViSP gốc là 1.177.942 cặp trên cả ba split. Validation và test được giữ để đánh giá; không gộp toàn bộ vào training. Nhóm còn 50 câu pilot và 12 câu nguồn chưa rõ nên không dùng cho train/dev/test. Chi tiết: data/visp_manifest.json và data/team_manifest.json.

Stage A học cặp giữ nghĩa bằng contrastive learning trên toàn bộ train ViSP hợp lệ. Các câu vượt 512 token được ghi thành danh sách loại, không cắt ngầm. Stage B học từ toàn bộ 697 nguồn train của nhóm: lựa chọn lịch sử thành preference yếu; độ trôi chảy và giữ nghĩa là nhãn teacher tự động. 141 nguồn dev chọn checkpoint và ngưỡng giữ câu gốc. 150 test cũ được ghi rõ là đánh giá hồi cứu.

Đã khóa thêm 240 câu test từ 12 truyện mới và 30 pilot từ 3 truyện khác, loại 45 truyện đã dùng trước đó. Sampling diễn ra trước khi có output model.

## Luồng thực thi

ViSP train hợp lệ → full encoder foundation → dữ liệu nhóm train → full evaluator → chọn checkpoint/ngưỡng trên dev → khóa model → đánh giá test và pipeline → đóng gói.

Nhánh đối chứng giữ nguyên dữ liệu nhóm và cách học, nhưng bắt đầu từ MiniLM ban đầu, bỏ stage A. Có thể so kết quả dev giữa hai nhánh để kiểm tra ích lợi của nền ViSP.

## Chạy trên Kaggle

Notebook: delivery/Vietnamese_Evaluator_Kaggle.ipynb. Notebook chứa code và dữ liệu nhóm, tự tải CSV ViSP công khai từ revision đã khóa. Bật Internet và GPU T4. Giữ notebook riêng tư. Gắn output version 370624086 của nettopro/visp-full-fine-tune-nlp501 để chạy so sánh generator cũ; script xác minh hash chính xác trước khi dùng.

Link dự án: https://www.kaggle.com/code/nettopro/vietnamese-evaluator-visp-team-full-training

Các lệnh được notebook thực thi:

~~~text
python download_data.py
python train.py a
python train.py b
python train.py ablation
python evaluate.py
python fresh_pipeline.py
python package.py
~~~

Latest checkpoint lưu model, optimizer, scheduler, scaler và RNG. Chạy lại cùng stage trên workspace đã khôi phục latest.pt để tiếp tục. Token caches và input corpus phải đúng manifest. Tải checkpoint từ run trước nếu tạo một Kaggle session mới; session mới không tự chứa optimizer của run trước.

## Bàn giao application sau khi run hoàn tất

Model evaluator chính: artifacts/stage_b/best/.

Sau khi giải nén gói inference, mở PowerShell ngay trong thư mục có inference.py. Cài môi trường CPU như sau; không cần kích hoạt môi trường bằng Activate.ps1:

~~~powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
~~~

Khi chạy các ví dụ dưới đây, dùng Python của môi trường đã cài đủ dependencies. GPU Kaggle sử dụng Torch 2.11.0; CPU local dùng Torch 2.6.0. Kiểm tra reload bằng model thật được ghi riêng trong verification, không suy ra từ kiểm thử tiny model.

~~~python
from inference import VietnameseEvaluator
evaluator = VietnameseEvaluator("checkpoint")
result = evaluator.score(
    "Hắn đối với chuyện này cảm thấy khó hiểu.",
    "Hắn cảm thấy chuyện này khó hiểu."
)
~~~

Output gồm rank_score (điểm xếp hạng thô), fluency_delta_proxy (ước lượng NLL nguồn trừ NLL đích), semantic_preservation_proxy (ước lượng cosine của teacher). Không gọi các số này là xác suất đúng hay điểm người chấm 0–100. grammar_score là null vì chưa có nhãn ngữ pháp riêng. context_used và human_validated luôn false.

Rank nên được so giữa các phương án cùng input. Trong lượt thực nghiệm hiện tại, rank head ưu tiên identity trên dev và gate chọn ngưỡng 1e9, dẫn tới 0 can thiệp. Model/API đã được huấn luyện và có thể xuất điểm proxy; kết quả này chưa chứng minh cải thiện tự động sửa câu. Không dùng điểm raw retrieval 100% hoặc kết quả giữ nguyên câu để tuyên bố độ tự nhiên đạt 100%.

Kết quả heldout hiện tại: semantic head có MAE khoảng 0,185 so với 0,044 của baseline luôn dự đoán 1; tương quan Spearman khoảng -0,473 với teacher trên các cặp output duy nhất. Vì vậy surrogate hiện được bàn giao như model nghiên cứu, chưa đủ bằng chứng để dùng làm metric chính. Chi tiết và tập con chỉ gồm câu được sửa nằm trong reports/surrogate_teacher_agreement.json.

Bộ teacher tham chiếu tự động cũng có trong gói, để nhóm tiếp tục chấm proxy bằng các model nguồn đã khóa:

~~~python
from teacher import Teacher
reference = Teacher(device="cpu")
scores = reference.pair("Câu đầu vào tiếng Việt.", "Phương án cần đánh giá.")
~~~

Teacher tải các model Hugging Face công khai ở lần chạy đầu, rồi dùng cache. fluency_target là chênh lệch NLL, semantic_target là cosine; đây vẫn là proxy tự động, human_validated=false. Teacher embedding dùng giới hạn 128 token theo cấu hình nguồn, không đo ngữ cảnh hay độ trung thành với nguyên tác tiếng Trung.

CLI nhận JSONL có source và candidate:

~~~text
python inference.py --checkpoint checkpoint --input input.jsonl --output scored.jsonl
~~~

API tùy chọn:

~~~powershell
python -m pip install fastapi uvicorn
$env:VI_EVALUATOR_CHECKPOINT = "checkpoint"
python -m uvicorn api:app --host 127.0.0.1 --port 8000
~~~

POST /score nhận source và candidate. Input rỗng hoặc vượt token limit bị trả lỗi 422. Mô hình hiện chỉ xem cặp câu, không dùng ngữ cảnh.

## Đọc kết quả đúng phạm vi

training_proof.json chứng minh số mẫu, số optimizer step và trọng số thực sự thay đổi. reports/stage_a_*_full.json đo retrieval giữ nghĩa trên ViSP, không đo độ tự nhiên bằng người đọc. reports/fresh_pipeline_report.json đo các proxy tự động trên tiếng Việt; không xác minh bản dịch có trung thành với nguyên tác tiếng Trung. Do teacher cũng cung cấp nhãn train, mức đồng ý với teacher chưa phải bằng chứng độc lập về cảm nhận của người đọc. Phần xác nhận bởi người đọc vẫn chờ.

ViSP có cặp thuận–nghịch, nên raw retrieval có thể được điểm nhờ tìm đúng câu giống hệt input. Script retrieval_audit.py chạy sau khi khóa model để bổ sung reports/stage_a_*_nonidentity.json, loại các ứng viên có token giống input và ghi rõ số query còn hợp lệ. Đây là sửa phép đo chẩn đoán sau khi nhận diện hiện tượng trùng, không thay đổi dữ liệu train, model hay cách chọn checkpoint. Pool vẫn có nhiều paraphrase cùng nhóm, nên cần đọc cả độ đa dạng nhóm trong report.

Gói inference chỉ được tạo khi cả hai stage, đối chứng và gate đã có proof. Kiểm tra verification/kaggle_run.json để biết trạng thái thực tế; không suy ra đã train xong từ việc có notebook.

Tham khảo chính thức: [ViSP dataset](https://huggingface.co/datasets/ngwgsang/ViSP), [JFLEG paper](https://aclanthology.org/E17-2037/), [SEEDA repository](https://github.com/tmu-nlp/SEEDA).
