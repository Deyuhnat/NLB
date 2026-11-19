# ViSP — Full fine-tune

**Cập nhật đánh giá đầu ra:** Đã có một lượt chấm bằng mô hình cho 300 phiếu câu và 515 edit. Xem `evaluation_model/KET_QUA_DANH_GIA.html`. Các phiếu người đọc gốc vẫn pending; lượt chấm mới được lưu riêng và không được xem như đánh giá người độc lập.

**Bộ dữ liệu gồm 1.050 câu đã được nhóm review**

Project này cập nhật toàn bộ trọng số ViSP; không dùng LoRA. JFLEG/SEEDA là cơ sở thiết kế đánh giá, không phải hai model riêng để train.

## Kaggle

Notebook riêng tư của lượt chạy: https://www.kaggle.com/code/nettopro/visp-full-fine-tune-nlp501

Version 2: https://www.kaggle.com/code/nettopro/visp-full-fine-tune-nlp501?scriptVersionId=370624086

**Kết quả đã xác nhận:** Version 2 hoàn tất thành công trên Tesla T4 trong 749,2 giây. Có full training proof, full weights, selected_model, test_metrics và kiểm tra nạp lại. Chọn LR=1e-5, epoch 1. Đọc `reports/KET_QUA_FULL_FINETUNE.html` để xem kết quả cùng giới hạn; chrF++ tăng từ 76,59 lên 89,79 so với ViSP gốc nhưng chưa vượt baseline giữ nguyên. Judgments độ tự nhiên/giữ nghĩa còn pending.

Mở tab Logs để xem trạng thái thực tế. Chỉ khi có `selected_model.json`, `test_metrics.json` và `reload_verification.json` mới kết luận đã hoàn tất train/evaluate. File `verification/kaggle_run.json` lưu bằng chứng trạng thái đã kiểm tra gần nhất.

`ViSP_Full_Finetune_Kaggle.ipynb` là bản tự chứa mã nguồn và dữ liệu, không cần database hoặc dataset phụ. Chọn GPU T4 và Internet rồi Save & Run All. Giữ notebook Private vì chứa corpus của nhóm. Model/checkpoint không tự động công bố lên Hugging Face.

## Dữ liệu

- Train: 697 cặp, gồm 221 target thay đổi và 476 target giữ nguyên.
- Dev: 141 cặp, gồm 73 thay đổi và 68 giữ nguyên.
- Test: 150 cặp, gồm 44 thay đổi và 106 giữ nguyên.
- Pilot và 13 mẫu nguồn chưa rõ bị tách khỏi thí nghiệm chính.
- Snapshot và work-wise split được kế thừa từ vi_selector. Dữ liệu không được chia lại để tăng điểm.
- Tên thành viên trong hệ thống thể hiện phân công; provenance review được giữ trong dữ liệu, không dùng làm đặc trưng và không được suy thành nhiều lượt đánh giá độc lập.

## Training

Input có prefix `sentence-paraphrase: `; target là bản đã duyệt, gồm cả bản sửa tay. Ngữ cảnh dành cho reviewer, chưa đưa vào input model.

Hai learning rate 1e-5 và 3e-5, seed 42, AdamW, FP32, effective batch 16, gradient checkpointing, tối đa 6 epoch. Mỗi epoch lấy mẫu cân bằng 476 lượt thay đổi và 476 lượt giữ nguyên, có hoàn lại. Chọn checkpoint bằng trung bình dev token loss của hai nhóm, không dùng test.

Model gốc được khóa tại revision `ff75dba118e7a175142d5daa9b893b44229c1f55`. Toàn bộ tham số được bật học. `full_training_proof.json` kiểm tra gradient và trọng số thực sự thay đổi sau bước có learning rate dương. Bước đầu của warmup có thể có learning rate 0 nên không dùng làm bằng chứng trọng số phải đổi.

`latest.pt` lưu model, optimizer, scheduler và RNG ở cuối epoch để resume trong cùng workspace. Nếu chuyển sang session Kaggle mới, phải tải/attach checkpoint cũ rồi đặt lại đúng thư mục; không chỉ chạy lại notebook rỗng rồi gọi là resume.

## Chạy mã nguồn

Trên môi trường có torch phù hợp GPU:

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_finetune
python full_finetune.py train --data data --output runs
python full_finetune.py evaluate --data data --output runs
```

Lệnh `train` chặn CPU để tránh vô tình train model lớn trên laptop. Smoke test chạy tiny T5 trên CPU để kiểm tra optimizer/nạp lại/resume; nó không phải kết quả fine-tune ViSP.

## Dùng model đã tải về trên Windows

Mở PowerShell trong thư mục này. `data/inference_example.jsonl` chứa ví dụ, mỗi dòng có sample_id và input_vi. Lệnh sau dùng CPU, không kết nối database:

```powershell
& .venv\Scripts\python.exe -X utf8 infer.py --model runs\lr_1e-05\best --input data\inference_example.jsonl --output reports\my_predictions.jsonl --device cpu
```

Nếu chuyển máy, cài Python, torch phù hợp CPU/GPU và requirements.txt trước. Inference không yêu cầu training lại. Không cần LoRA adapter; thư mục best chứa full model. Chỉ checkpoint tốt nhất được tải về local; các latest.pt để resume vẫn có trong output Kaggle (tổng output khoảng 7,24 GB).

Đã kiểm tra nạp full weights trên CPU Windows và sinh ba câu: 3/3 raw output trùng Kaggle. Bằng chứng ở `verification/local_full_model_reload.json`. SHA-256 weights được đối chiếu trong `verification/final_verification.json`.

Hai gói bàn giao `ViSP_Full_Finetune_Source_Results.zip` và `ViSP_Full_Finetune_Weights.zip` cần được giải nén vào cùng một thư mục cha; chúng sẽ ghép thành `visp_finetune/`. Gói source/results nhỏ, gói weights khoảng 904 MB. Thư mục project hiện tại đã có đủ cả hai phần.

## Đầu ra

- `runs/lr_*/best/`: full weights và tokenizer của checkpoint tốt nhất mỗi learning rate.
- `runs/lr_*/latest.pt`: checkpoint để resume cuối epoch.
- `runs/selected_model.json`: model được chọn theo dev.
- `runs/test_predictions.jsonl`: output trước/sau trên cùng test.
- `runs/test_metrics.json`: chrF++, exact match, can thiệp và lỗi sinh; tách nhóm thay đổi/giữ nguyên.
- `runs/reload_verification.json`: kiểm tra nạp lại model cho cùng output.
- `runs/evaluation/`: phiếu A/B, các edit và mapping riêng.

Không dùng ba ứng viên beam-sampling cũ làm baseline trực tiếp cho beam-search mới. Baseline ViSP gốc được sinh lại cùng decoding với model fine-tune: beam 5, không sampling, 1 output.

## Đánh giá JFLEG/SEEDA

Phiếu câu chấm độ tự nhiên 1–5, giữ nghĩa, harm và ưu tiên A/B. Nhãn `needs_edit` phải được chấm, không lấy từ việc target có thay đổi. Phiếu edit dùng offset Unicode code point, start từ 0, end loại trừ; đây là căn chỉnh ký tự, không phải phân tích lỗi ngữ nghĩa tự động.

Giữ `private_key.json` khỏi reviewer tới khi chấm xong. Hai người chấm riêng, sau đó phân xử thành một file cuối để chạy scorer. `score_judgments.py` tính các metric chất lượng khi đủ nhãn. Không có judgments thì các mục safe improvement/harm/clean harm để pending/null.

Test đã được xem trong lượt bộ chọn trước. Đây là so sánh hồi cứu trên tác phẩm giữ riêng, chưa phải benchmark mù mới. Corpus thuộc miền truyện tiên hiệp/kỳ ảo/huyền huyễn; chưa thực hiện benchmark nguồn Trung và bản dịch chuyên nghiệp trong hình thảo luận.

## Giới hạn

Không bảo đảm full fine-tune tốt hơn model gốc. Corpus nhỏ và nhiều target giữ nguyên nên cần đọc cả tỷ lệ can thiệp, nhóm target thay đổi và judgments, không chỉ exact match. Cờ số/phủ định và độ giống reference không xác nhận đầy đủ giữ nghĩa.
