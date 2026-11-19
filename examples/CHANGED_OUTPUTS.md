# Output có thay đổi — ví dụ chạy thật

Trong test hồi cứu, ViSP fine-tune thay đổi **57/150 câu (38%)**, giữ nguyên 93 câu. Ba ví dụ dưới được chọn để thấy thay đổi; không dùng chúng để ước lượng chất lượng tổng thể. Có cả ví dụ lỗi mất ý.

**[JSON và output gốc](changed_outputs.json)** · [Sample đầy đủ kèm evaluator](README.md)

## Ví dụ 1

**Input:**

> Chỉ là Tần Trường Sinh vốn không có ý định bán linh mễ.

**Output ViSP:**

> Tần Trường Sinh vốn không có ý định bán linh mễ.

**Nhận xét khi đối chiếu:** Bỏ cụm “Chỉ là”. Có thay đổi, nhưng cần ngữ cảnh để quyết định có nên bỏ từ nối hay không.

## Ví dụ 2

**Input:**

> Hơn nữa Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần.

**Output ViSP:**

> Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần.

**Nhận xét khi đối chiếu:** Bỏ cụm “Hơn nữa”. Đây là rút gọn từ nối, chưa chứng minh câu tốt hơn.

## Ví dụ 3

**Input:**

> Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, muốn thu thập về tặng cho mẹ, nên mới lên tiếng.

**Output ViSP:**

> Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, nên mới lên tiếng.

**Nhận xét khi đối chiếu:** LỖI MẤT Ý: bỏ mục đích “muốn thu thập về tặng cho mẹ”. Không nên chấp nhận output này.

## Vì sao nhiều câu giữ nguyên?

Train generator có 697 cặp: 476 target giữ nguyên và 221 target thay đổi. Vì vậy mô hình học nhiều trường hợp cần giữ nguyên; tỷ lệ này phù hợp với xu hướng can thiệp ít hiện thấy, nhưng chưa chứng minh nguyên nhân duy nhất. Câu không đổi ở generator khác với gate evaluator giữ câu gốc.

Các ví dụ trên là output generator trước gate. Chưa chạy evaluator riêng cho phần bổ sung này (`evaluation=null`), không gán điểm giả. Mất ý như ví dụ 3 là lý do cần người đọc duyệt và chưa nên tự động áp dụng sửa câu.
