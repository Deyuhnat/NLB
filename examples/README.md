# Sample output thật: ViSP → evaluator

Ba câu dưới đây lấy từ lượt sinh ViSP trên CPU đã lưu; evaluator được chạy thật trên CPU để chấm các cặp này. Không chỉnh sửa câu trả về để làm ví dụ đẹp hơn. Đây là ví dụ định dạng và hành vi, **không phải benchmark chất lượng độc lập**.

**[Xem JSON đầy đủ cho application](sample_output.json)** · [Hướng dẫn chạy](../README.md)

ViSP có thể giữ nguyên input. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật, không chứng minh câu hay hơn. Điểm evaluator là proxy chưa hiệu chuẩn; phiên bản hiện tại chưa nên làm metric chính.

## Ví dụ 1

**Input:**

> Tần Trường Sinh hiểu rất rõ, một khi mối liên hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân.

**Output ViSP:**

> Tần Trường Sinh hiểu rất rõ, một khi mối quan hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân.

**Hành vi:** Có chỉnh sửa; `status=ok`, `fallback=false`.

| Điểm evaluator thực tế | Giá trị |
|---|---|
| rank_score | 0.037410 |
| fluency_delta_proxy | 0.066931 |
| semantic_preservation_proxy | 0.805124 |
| grammar_score | null |
| human_validated / context_used | false / false |

## Ví dụ 2

**Input:**

> Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa.

**Output ViSP:**

> Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa.

**Hành vi:** Giữ nguyên câu gốc; `status=ok`, `fallback=false`.

| Điểm evaluator thực tế | Giá trị |
|---|---|
| rank_score | -0.331434 |
| fluency_delta_proxy | 0.065685 |
| semantic_preservation_proxy | 0.854465 |
| grammar_score | null |
| human_validated / context_used | false / false |

## Ví dụ 3

**Input:**

> Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: "Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!"

**Output ViSP:**

> Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: "Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!"

**Hành vi:** Giữ nguyên câu gốc; `status=ok`, `fallback=false`.

| Điểm evaluator thực tế | Giá trị |
|---|---|
| rank_score | 0.178512 |
| fluency_delta_proxy | 0.061545 |
| semantic_preservation_proxy | 0.585644 |
| grammar_score | null |
| human_validated / context_used | false / false |

## Teammate dùng sample này như thế nào?

- Xem `source` và `candidate` để dựng màn hình đối chiếu câu gốc/phương án.
- Giữ `generator.status`, `fallback`, `error`; không biến fallback thành một cải thiện thành công.
- Đọc điểm trong `evaluation`; không diễn giải thành xác suất hay điểm người đọc 0–100.
- Giữ `sample_id` để ghép dữ liệu. Khi chạy lại, timing và sai số số thực có thể khác theo máy/batch.
- Theo luồng ba lệnh trong README để tự sinh output mới từ checkpoint trong Release.
