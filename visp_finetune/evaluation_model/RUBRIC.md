# Rubric đánh giá output theo hướng JFLEG/SEEDA

Đây là một lượt đánh giá bằng mô hình có hỗ trợ đọc ngữ cảnh, reviewer_id=codex_model_review. Không phải đánh giá của người độc lập, không phải tái chạy benchmark tiếng Anh JFLEG/SEEDA gốc. Cùng trợ lý đã tham gia review dữ liệu trước train nên lượt đánh giá này có phụ thuộc vào quá trình tạo nhãn. Không dùng tên thành viên để tính đồng thuận giữa người chấm.

## Mức câu

- Đơn vị: một câu input, ngữ cảnh trước/sau và một output. Hai output/câu được ký hiệu X/Y; mapping được giữ để tái lập. Việc đổi ký hiệu không bảo đảm mù hoàn toàn vì người đánh giá đã biết thiết kế và kết quả hệ thống.
- needs_edit được đánh giá trên input và ngữ cảnh, không suy từ target khác input. Hai phiếu cùng input dùng cùng nhãn input.
- Độ tự nhiên 1–5: 1 khó hiểu/hỏng cấu trúc hoặc lặp nghiêm trọng; 2 gượng nặng; 3 hiểu được nhưng còn chỗ gượng cần sửa; 4 chấp nhận được trong văn phong truyện, có điểm nhỏ; 5 tự nhiên và rõ trong ngữ cảnh. Điểm này tách khỏi giữ nghĩa: output trôi chảy vẫn có thể đổi nội dung.
- needs_edit=true khi có vấn đề diễn đạt/punctuation cần sửa, bao gồm lỗi nhỏ ở input điểm 4; không mặc định mọi câu điểm 4 cần sửa.
- Bảo toàn: preserved / minor_change / major_change / uncertain. Minor gồm mất sắc thái hoặc chi tiết nhỏ; major gồm đổi chủ thể, đảo số lượng/yêu cầu, đổi câu hỏi thành sự thật, bỏ mệnh đề quan trọng. Uncertain khi nguồn quá gượng không đủ căn cứ quyết định.
- Harm khi giảm độ tự nhiên hoặc thay đổi nội dung/trình bày gây hại. Không tự coi mọi minor_change là harmful. Việc bỏ chi tiết quan trọng, đổi vai và cấu trúc thoại bị đánh dấu riêng trong nhận xét.
- Lời thoại phải được xem cùng ngữ cảnh. Câu bị tách ở giữa lời thoại không tự bị trừ điểm vì thiếu cặp quote trong riêng dòng đó. Nếu model xóa dấu mở/đóng khiến đoạn hội thoại không khớp thì bị đánh dấu lỗi trình bày. Đổi dấu cảm thán thành chấm trong trần thuật không tự động là harm.
- Ưu tiên input/output/tie dựa cả nghĩa lẫn tự nhiên; content fidelity được ưu tiên khi có thay đổi gây hại. Input=output luôn tie, cùng điểm, preserved và không harmful.
- Safe improvement chỉ khi input cần sửa, output tự nhiên hơn, preserved và không harmful.

## Mức edit

- Có 515 edit theo SequenceMatcher ở mức ký tự; start=0, end loại trừ, Unicode code points. Đây là đơn vị căn chỉnh kỹ thuật, không phải 515 lỗi ngữ nghĩa độc lập.
- Đọc cả input/output/ngữ cảnh trước khi đánh giá mỗi edit. Các mảnh của cùng một thay đổi từ hoặc vế câu được xem cùng nhau; không đoán nghĩa chỉ từ mảnh ký tự.
- accepted: thay đổi chấp nhận được và không gây hại trong output; không đồng nghĩa edit đó cần thiết hoặc cải thiện.
- rejected: thay đổi gây lỗi nội dung, mất chi tiết cần giữ, lỗi cú pháp/lặp hoặc cấu trúc thoại. uncertain: không đủ căn cứ.
- Một output có thể có cả edit accepted và rejected. Một minor_change không gây hại có thể có edit accepted nhưng không đủ điều kiện cải thiện an toàn ở mức câu.
- Nhận xét ở review_notes giải thích toàn thay đổi của mỗi variant. Không coi các edit của cùng câu là quan sát độc lập để tính độ chắc chắn thống kê.

## Mẫu số và giới hạn

Metric mức câu loại uncertain và báo riêng số loại; mẫu số zero trả null. Edit precision toàn tập chỉ công bố khi không còn uncertain/pending; luôn báo accepted/rejected/uncertain và precision trên phần confirmed.

Không huấn luyện hay điều chỉnh lại model từ những nhãn test này. Muốn dùng nhãn để phát triển tiếp phải ghi vòng thăm dò và có test mới cho kết luận cuối. Các phiếu người chấm gốc trong runs/evaluation vẫn pending và được giữ nguyên.
