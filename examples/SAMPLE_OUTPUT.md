# Sample output chung — ViSP và evaluator

**Có 30 ví dụ:** 20 câu có thay đổi và 10 câu giữ nguyên. Đây là bộ minh họa được chọn có chủ đích, không đại diện tỷ lệ chất lượng toàn test. Sáu ví dụ ban đầu được giữ nguyên thứ tự.

Output ViSP và điểm evaluator được chạy thật. Mỗi ví dụ có **quyết định tiếng Việt của bộ chọn** và câu cuối cùng. Phần quyết định là diễn giải quy tắc rank/gate, không phải lời giải thích ngữ nghĩa do model sinh.

Ngưỡng gate hiện tại là `1e9`: chỉ chọn phương án nếu rank(phương án) − rank(câu gốc) vượt ngưỡng. Bộ chọn hiện rất bảo thủ; giữ câu gốc chưa chứng minh phát hiện được lỗi mất ý. **Các điểm chưa phù hợp làm metric chính.**

Đánh dấu: ~~phần bị xóa~~ ở câu gốc; **phần thêm** ở output. Test hồi cứu có 57/150 output thay đổi (38%); các ví dụ này không phải phép đo chất lượng độc lập.

[Hướng dẫn chạy](../README.md)

## Ví dụ 1

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Tần Trường Sinh hiểu rất rõ, một khi mối <del>liên</del> hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân. |
| Output ViSP | Tần Trường Sinh hiểu rất rõ, một khi mối <strong>quan</strong> hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Tần Trường Sinh hiểu rất rõ, một khi mối liên hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.041008 | 0.037410 |
| fluency_delta_proxy | 0.066646 | 0.066931 |
| semantic_preservation_proxy | 0.804051 | 0.805124 |

Chênh lệch rank: `-0.003598`; ngưỡng gate: `1e+09`.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 2

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa. |
| Output ViSP | Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa.

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.331434 | -0.331434 |
| fluency_delta_proxy | 0.065685 | 0.065685 |
| semantic_preservation_proxy | 0.854465 | 0.854465 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 3

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: &quot;Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!&quot; |
| Output ViSP | Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: &quot;Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!&quot; |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: "Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!"

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.178512 | 0.178512 |
| fluency_delta_proxy | 0.061545 | 0.061545 |
| semantic_preservation_proxy | 0.585644 | 0.585644 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 4

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | <del>Chỉ là</del> Tần Trường Sinh vốn không có ý định bán linh mễ. |
| Output ViSP | Tần Trường Sinh vốn không có ý định bán linh mễ. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Chỉ là Tần Trường Sinh vốn không có ý định bán linh mễ.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.364870 | -0.464668 |
| fluency_delta_proxy | 0.066543 | 0.072019 |
| semantic_preservation_proxy | 0.797392 | 0.806176 |

Chênh lệch rank: `-0.099798`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Bỏ cụm “Chỉ là”. Có thay đổi, nhưng cần ngữ cảnh để quyết định có nên bỏ từ nối hay không.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 5

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | <del>Hơn nữa</del> Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần. |
| Output ViSP | Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Hơn nữa Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.372729 | -0.428376 |
| fluency_delta_proxy | 0.063842 | 0.066372 |
| semantic_preservation_proxy | 0.762824 | 0.776063 |

Chênh lệch rank: `-0.055647`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Bỏ cụm “Hơn nữa”. Đây là rút gọn từ nối, chưa chứng minh câu tốt hơn.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 6

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, <del>muốn thu thập về tặng cho mẹ,</del> nên mới lên tiếng. |
| Output ViSP | Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, nên mới lên tiếng. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, muốn thu thập về tặng cho mẹ, nên mới lên tiếng.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.292058 | -0.523073 |
| fluency_delta_proxy | 0.062793 | 0.075771 |
| semantic_preservation_proxy | 0.859860 | 0.872217 |

Chênh lệch rank: `-0.231015`; ngưỡng gate: `1e+09`.

**Nhận xét khi đọc câu:** output mất mục đích “muốn thu thập về tặng cho mẹ”. Rank ưu tiên câu gốc nhưng head semantic lại chấm output mất ý cao hơn. Vì vậy quyết định giữ câu gốc ở đây không chứng minh model hiểu lỗi mất ý.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 7

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Chàng vô thức đưa tay cầm lấy một lá, cảm nhận được hơi ấm và linh khí quen thuộc, lại lật xem bốn lá còn <del>lại, tất cả đều là Hỏa Đạn Phù thành phẩm thực thụ, tuyệt đối không phải ảo giác.</del> |
| Output ViSP | Chàng vô thức đưa tay cầm lấy một lá, cảm nhận được hơi ấm và linh khí quen thuộc, lại lật xem bốn lá còn <strong>lại.</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Chàng vô thức đưa tay cầm lấy một lá, cảm nhận được hơi ấm và linh khí quen thuộc, lại lật xem bốn lá còn lại, tất cả đều là Hỏa Đạn Phù thành phẩm thực thụ, tuyệt đối không phải ảo giác.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.121694 | -0.646637 |
| fluency_delta_proxy | 0.062393 | 0.112122 |
| semantic_preservation_proxy | 0.716701 | 0.906764 |

Chênh lệch rank: `-0.768331`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 8

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | <del>Trong sách ghi chép,</del> Ma Yêu là một loại yêu quái, là dã thú sau khi ăn phải máu thịt của người hoặc vật nhiễm phải thứ quỷ dị, bị luồng sức mạnh đó làm cho biến dị mà thành! |
| Output ViSP | Ma Yêu là một loại yêu quái, là dã thú sau khi ăn phải máu thịt của người hoặc vật nhiễm phải thứ quỷ dị, bị luồng sức mạnh đó làm cho biến dị mà thành! |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Trong sách ghi chép, Ma Yêu là một loại yêu quái, là dã thú sau khi ăn phải máu thịt của người hoặc vật nhiễm phải thứ quỷ dị, bị luồng sức mạnh đó làm cho biến dị mà thành!

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.167722 | 0.123678 |
| fluency_delta_proxy | 0.062184 | 0.066605 |
| semantic_preservation_proxy | 0.615036 | 0.637908 |

Chênh lệch rank: `-0.044045`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 9

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Vương Tùng bước lên trước một bước, <del>lập tức</del> chắp tay với Trần Quan: <del>“Tiêu</del> sư Trần, dọc đường vất vả rồi, mau mau mời <del>vào!”</del> |
| Output ViSP | Vương Tùng bước lên trước một bước, chắp tay với Trần Quan: <strong>Tiêu</strong> sư Trần, dọc đường vất vả rồi, mau mau mời <strong>vào!</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Vương Tùng bước lên trước một bước, lập tức chắp tay với Trần Quan: “Tiêu sư Trần, dọc đường vất vả rồi, mau mau mời vào!”

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.168471 | 0.102122 |
| fluency_delta_proxy | 0.062106 | 0.068174 |
| semantic_preservation_proxy | 0.616457 | 0.652386 |

Chênh lệch rank: `-0.066349`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 10

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Khi nét bút cuối cùng hạ xuống, mặt giấy bùa <del>đột nhiên</del> bừng lên một tầng hồng quang ấm áp, linh khí dao động bỗng chốc ngưng tụ, một lá Hỏa Đạn Phù hoàn chỉnh vững vàng rơi xuống mặt bàn, thân bùa hơi nóng lên, <del>toả</del> ra khí tức tấn công đầy nội liễm. |
| Output ViSP | Khi nét bút cuối cùng hạ xuống, mặt giấy bùa <strong>bỗng</strong> bừng lên một tầng hồng quang ấm áp, linh khí dao động bỗng chốc ngưng tụ, một lá Hỏa Đạn Phù hoàn chỉnh vững vàng rơi xuống mặt bàn, thân bùa hơi nóng lên, <strong>tỏa</strong> ra khí tức tấn công đầy nội liễm. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Khi nét bút cuối cùng hạ xuống, mặt giấy bùa đột nhiên bừng lên một tầng hồng quang ấm áp, linh khí dao động bỗng chốc ngưng tụ, một lá Hỏa Đạn Phù hoàn chỉnh vững vàng rơi xuống mặt bàn, thân bùa hơi nóng lên, toả ra khí tức tấn công đầy nội liễm.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.166818 | 0.160408 |
| fluency_delta_proxy | 0.061120 | 0.061679 |
| semantic_preservation_proxy | 0.616115 | 0.621812 |

Chênh lệch rank: `-0.006410`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 11

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Tần Trường Sinh giả vờ nghi hoặc hỏi: &quot;Các hạ <del>là?&quot;</del> |
| Output ViSP | Tần Trường Sinh giả vờ nghi hoặc hỏi: &quot;Các hạ <strong>là ai?&quot;</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Tần Trường Sinh giả vờ nghi hoặc hỏi: "Các hạ là?"

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.058285 | 0.035147 |
| fluency_delta_proxy | 0.064988 | 0.067105 |
| semantic_preservation_proxy | 0.749697 | 0.762248 |

Chênh lệch rank: `-0.023138`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 12

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Trương Viễn nghe theo lời Tần Trường Sinh, thay <del>lên</del> y phục của đệ tử tạp dịch. |
| Output ViSP | Trương Viễn nghe theo lời Tần Trường Sinh, thay y phục của đệ tử tạp dịch. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Trương Viễn nghe theo lời Tần Trường Sinh, thay lên y phục của đệ tử tạp dịch.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.374135 | -0.392029 |
| fluency_delta_proxy | 0.062271 | 0.064212 |
| semantic_preservation_proxy | 0.766369 | 0.782109 |

Chênh lệch rank: `-0.017895`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 13

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Mà sự tiến bộ trên con đường chế phù, càng khiến chính Tần Trường Sinh <del>cũng</del> phải kinh ngạc không thôi. |
| Output ViSP | Mà sự tiến bộ trên con đường chế phù, càng khiến chính Tần Trường Sinh phải kinh ngạc không thôi. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Mà sự tiến bộ trên con đường chế phù, càng khiến chính Tần Trường Sinh cũng phải kinh ngạc không thôi.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.244215 | -0.397211 |
| fluency_delta_proxy | 0.068916 | 0.077439 |
| semantic_preservation_proxy | 0.883798 | 0.895635 |

Chênh lệch rank: `-0.152996`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 14

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Hắn còn chưa kịp thốt ra một tiếng kêu thảm, máu tươi đã trào ra từ miệng và mũi, mất <del>sạch</del> khả năng chiến đấu. |
| Output ViSP | Hắn còn chưa kịp thốt ra một tiếng kêu thảm, máu tươi đã trào ra từ miệng và mũi, mất <strong>hết</strong> khả năng chiến đấu. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Hắn còn chưa kịp thốt ra một tiếng kêu thảm, máu tươi đã trào ra từ miệng và mũi, mất sạch khả năng chiến đấu.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.201895 | -0.212468 |
| fluency_delta_proxy | 0.068993 | 0.070635 |
| semantic_preservation_proxy | 0.881406 | 0.886880 |

Chênh lệch rank: `-0.010574`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 15

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Khi bán cố gắng tránh người quen, nếu cần giao dịch thì chỉ bàn chuyện làm ăn, không nên tán gẫu <del>nhiều.&quot;</del> |
| Output ViSP | Khi bán cố gắng tránh <strong>xa</strong> người quen, nếu cần giao dịch thì chỉ bàn chuyện làm ăn, không nên tán gẫu <strong>nhiều.</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Khi bán cố gắng tránh người quen, nếu cần giao dịch thì chỉ bàn chuyện làm ăn, không nên tán gẫu nhiều."

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.138548 | -0.645321 |
| fluency_delta_proxy | 0.063261 | 0.116556 |
| semantic_preservation_proxy | 0.683097 | 0.905257 |

Chênh lệch rank: `-0.783869`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 16

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | <del>“Các</del> huynh nói nơi thi đấu sẽ có rất nhiều hoa đẹp là thật <del>sao?”</del> |
| Output ViSP | <strong>Các</strong> huynh nói nơi thi đấu sẽ có rất nhiều hoa đẹp là thật <strong>sao?</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> “Các huynh nói nơi thi đấu sẽ có rất nhiều hoa đẹp là thật sao?”

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.166547 | -0.712000 |
| fluency_delta_proxy | 0.062161 | 0.121903 |
| semantic_preservation_proxy | 0.611501 | 0.880529 |

Chênh lệch rank: `-0.878547`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 17

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Trả thù cho lão Lưu, lão Vương <del>đi!!”</del> |
| Output ViSP | Trả thù cho lão Lưu, lão Vương <strong>đi!!</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Trả thù cho lão Lưu, lão Vương đi!!”

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.081565 | -0.127580 |
| fluency_delta_proxy | 0.068716 | 0.086740 |
| semantic_preservation_proxy | 0.723246 | 0.786930 |

Chênh lệch rank: `-0.209145`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 18

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | <del>“Nàng</del> Nàng, sắp đến lúc con tham gia thi đấu rồi, sao con chẳng sốt ruột chút nào <del>vậy!”</del> |
| Output ViSP | <strong>Nàng</strong> Nàng, sắp đến lúc con tham gia thi đấu rồi, sao con chẳng sốt ruột chút nào <strong>vậy!</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> “Nàng Nàng, sắp đến lúc con tham gia thi đấu rồi, sao con chẳng sốt ruột chút nào vậy!”

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.178185 | 0.050883 |
| fluency_delta_proxy | 0.061850 | 0.074218 |
| semantic_preservation_proxy | 0.589324 | 0.669979 |

Chênh lệch rank: `-0.127301`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 19

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Lưu Na trực tiếp đánh người ta tàn phế luôn <del>đó.”</del> |
| Output ViSP | Lưu Na trực tiếp đánh người ta tàn phế luôn <strong>đó.</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Lưu Na trực tiếp đánh người ta tàn phế luôn đó.”

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.010741 | -0.912900 |
| fluency_delta_proxy | 0.067735 | 0.124170 |
| semantic_preservation_proxy | 0.799526 | 0.911632 |

Chênh lệch rank: `-0.923641`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 20

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Nghe vậy, Lâm Hạo Phàm chỉ đành cười khổ lắc đầu: <del>“Đợi</del> con đột phá cảnh giới Thánh Hoàng thì cha mới có thể dẫn Niệm Niệm đi được, nếu không mẹ sẽ giận đó, Niệm Niệm đợi thêm chút nữa có được <del>không.”</del> |
| Output ViSP | Nghe vậy, Lâm Hạo Phàm chỉ đành cười khổ lắc đầu: <strong>Đợi</strong> con đột phá cảnh giới Thánh Hoàng thì cha mới có thể dẫn Niệm Niệm đi được, nếu không mẹ sẽ giận đó, Niệm Niệm đợi thêm chút nữa có được <strong>không?</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Nghe vậy, Lâm Hạo Phàm chỉ đành cười khổ lắc đầu: “Đợi con đột phá cảnh giới Thánh Hoàng thì cha mới có thể dẫn Niệm Niệm đi được, nếu không mẹ sẽ giận đó, Niệm Niệm đợi thêm chút nữa có được không.”

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.182408 | 0.081419 |
| fluency_delta_proxy | 0.060134 | 0.068204 |
| semantic_preservation_proxy | 0.584076 | 0.645513 |

Chênh lệch rank: `-0.100989`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 21

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Một tên thuộc hạ bên cạnh hắn cũng tặc lưỡi kinh ngạc, <del>“Đây</del> chính là người duy nhất sống sót đi đến dưới chân thành Vọng Nguyệt trong suốt nửa tháng <del>qua!”</del> |
| Output ViSP | Một tên thuộc hạ bên cạnh hắn cũng tặc lưỡi kinh ngạc, <strong>Đây</strong> chính là người duy nhất sống sót đi đến dưới chân thành Vọng Nguyệt trong suốt nửa tháng <strong>qua!</strong> |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Một tên thuộc hạ bên cạnh hắn cũng tặc lưỡi kinh ngạc, “Đây chính là người duy nhất sống sót đi đến dưới chân thành Vọng Nguyệt trong suốt nửa tháng qua!”

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.182474 | 0.120079 |
| fluency_delta_proxy | 0.061726 | 0.067709 |
| semantic_preservation_proxy | 0.580528 | 0.620719 |

Chênh lệch rank: `-0.062395`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 22

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Trên bàn vốn chỉ có một lá Hỏa Đạn Phù, vậy mà với tốc độ mắt thường có thể thấy được, nó tự phân tách <del>ra</del> thêm bốn lá bùa y hệt, cộng với lá ban đầu, năm lá Hỏa Đạn Phù xếp chồng ngay ngắn lên nhau, hồng quang và linh khí dao động của mỗi lá đều không sai biệt chút nào, phẩm chất hoàn toàn đồng nhất. |
| Output ViSP | Trên bàn vốn chỉ có một lá Hỏa Đạn Phù, vậy mà với tốc độ mắt thường có thể thấy được, nó tự phân tách thêm bốn lá bùa y hệt, cộng với lá ban đầu, năm lá Hỏa Đạn Phù xếp chồng ngay ngắn lên nhau, hồng quang và linh khí dao động của mỗi lá đều không sai biệt chút nào, phẩm chất hoàn toàn đồng nhất. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Trên bàn vốn chỉ có một lá Hỏa Đạn Phù, vậy mà với tốc độ mắt thường có thể thấy được, nó tự phân tách ra thêm bốn lá bùa y hệt, cộng với lá ban đầu, năm lá Hỏa Đạn Phù xếp chồng ngay ngắn lên nhau, hồng quang và linh khí dao động của mỗi lá đều không sai biệt chút nào, phẩm chất hoàn toàn đồng nhất.

**Lý do theo điểm và gate:** Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.165689 | 0.158640 |
| fluency_delta_proxy | 0.061455 | 0.062137 |
| semantic_preservation_proxy | 0.621390 | 0.627653 |

Chênh lệch rank: `-0.007049`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 23

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | &quot;Nhiệm vụ hàng đầu của ngươi là đến phường thị bán Hỏa Đạn Phù.&quot; |
| Output ViSP | &quot;Nhiệm vụ hàng đầu của ngươi là đến phường thị bán Hỏa Đạn Phù.&quot; |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> "Nhiệm vụ hàng đầu của ngươi là đến phường thị bán Hỏa Đạn Phù."

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.151275 | 0.151275 |
| fluency_delta_proxy | 0.063073 | 0.063073 |
| semantic_preservation_proxy | 0.636377 | 0.636377 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Output trùng câu gốc; không có sửa đổi để áp dụng.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 24

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Tần Trường Sinh trong lòng cười lạnh, tình hình cá cực tốt ư? |
| Output ViSP | Tần Trường Sinh trong lòng cười lạnh, tình hình cá cực tốt ư? |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Tần Trường Sinh trong lòng cười lạnh, tình hình cá cực tốt ư?

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.042663 | 0.042663 |
| fluency_delta_proxy | 0.067785 | 0.067785 |
| semantic_preservation_proxy | 0.770192 | 0.770192 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Output trùng câu gốc; không có sửa đổi để áp dụng.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 25

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Lạc Ly bực bội lườm hắn một cái, &quot;Làm ta giật cả mình.&quot; |
| Output ViSP | Lạc Ly bực bội lườm hắn một cái, &quot;Làm ta giật cả mình.&quot; |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Lạc Ly bực bội lườm hắn một cái, "Làm ta giật cả mình."

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | 0.069958 | 0.069958 |
| fluency_delta_proxy | 0.066974 | 0.066974 |
| semantic_preservation_proxy | 0.774025 | 0.774025 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Output trùng câu gốc; không có sửa đổi để áp dụng.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 26

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Điều quý giá hơn là, bùa hỏa đạn ở cảnh giới đại thành có uy lực tăng hơn ba phần so với bùa chú cùng cấp. |
| Output ViSP | Điều quý giá hơn là, bùa hỏa đạn ở cảnh giới đại thành có uy lực tăng hơn ba phần so với bùa chú cùng cấp. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Điều quý giá hơn là, bùa hỏa đạn ở cảnh giới đại thành có uy lực tăng hơn ba phần so với bùa chú cùng cấp.

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.324266 | -0.324266 |
| fluency_delta_proxy | 0.067786 | 0.067786 |
| semantic_preservation_proxy | 0.841441 | 0.841441 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Output trùng câu gốc; không có sửa đổi để áp dụng.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 27

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Con ma sói ngửi thấy mùi máu thịt của người và ngựa phía trước, đôi mắt đỏ ngầu lập tức ánh lên vẻ tham lam. |
| Output ViSP | Con ma sói ngửi thấy mùi máu thịt của người và ngựa phía trước, đôi mắt đỏ ngầu lập tức ánh lên vẻ tham lam. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Con ma sói ngửi thấy mùi máu thịt của người và ngựa phía trước, đôi mắt đỏ ngầu lập tức ánh lên vẻ tham lam.

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.346176 | -0.346176 |
| fluency_delta_proxy | 0.061251 | 0.061251 |
| semantic_preservation_proxy | 0.825738 | 0.825738 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Output trùng câu gốc; không có sửa đổi để áp dụng.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 28

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Lâm Hạo Phàm xoa đầu con gái ngoan an ủi. |
| Output ViSP | Lâm Hạo Phàm xoa đầu con gái ngoan an ủi. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Lâm Hạo Phàm xoa đầu con gái ngoan an ủi.

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.365558 | -0.365558 |
| fluency_delta_proxy | 0.063222 | 0.063222 |
| semantic_preservation_proxy | 0.771202 | 0.771202 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Output trùng câu gốc; không có sửa đổi để áp dụng.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 29

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Tần Trường Sinh hít sâu một hơi, cúi người vung liềm. |
| Output ViSP | Tần Trường Sinh hít sâu một hơi, cúi người vung liềm. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Tần Trường Sinh hít sâu một hơi, cúi người vung liềm.

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.367532 | -0.367532 |
| fluency_delta_proxy | 0.064659 | 0.064659 |
| semantic_preservation_proxy | 0.807772 | 0.807772 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Output trùng câu gốc; không có sửa đổi để áp dụng.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## Ví dụ 30

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Kết quả là thứ mà mình tự hào, trong mắt kẻ địch lại chỉ là rác rưởi. |
| Output ViSP | Kết quả là thứ mà mình tự hào, trong mắt kẻ địch lại chỉ là rác rưởi. |

### Quyết định của bộ chọn

**GIỮ CÂU GỐC**

**Câu cuối cùng:**

> Kết quả là thứ mà mình tự hào, trong mắt kẻ địch lại chỉ là rác rưởi.

**Lý do theo điểm và gate:** Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.

| Điểm thực tế | Câu gốc | Phương án ViSP |
|---|---|
| rank_score | -0.359875 | -0.359875 |
| fluency_delta_proxy | 0.066429 | 0.066429 |
| semantic_preservation_proxy | 0.795335 | 0.795335 |

Chênh lệch rank: `0.000000`; ngưỡng gate: `1e+09`.

**Nhận xét khi đối chiếu:** Output trùng câu gốc; không có sửa đổi để áp dụng.

Trạng thái generator: `status=ok`, `fallback=false`. `status=ok` chỉ nghĩa sinh thành công về kỹ thuật.

## JSON đầy đủ trong cùng file

Application có thể đọc `decision.action`, `decision.decision_vi`, `decision.reason_vi`, `decision.selected_text`. Các trường này minh họa lớp quyết định áp dụng sau scoring; API `/score` hiện tại vẫn chỉ trả điểm, chưa tự trả các trường quyết định mới này.

<details>
<summary>Xem JSON của 6 sample, điểm và quyết định</summary>

```json
{
  "scored_examples_metadata": {
    "checkpoint_origin": "Published handoff ZIP checkpoint",
    "evaluator_version": "7b45b3a236b099d7",
    "device": "cpu",
    "sample_count": 30,
    "all_examples_rescored_with_identity": true,
    "human_validated": false
  },
  "changed_examples_metadata": {
    "origin": "Stored historical test predictions, not newly generated or an independent new test.",
    "changed_outputs": 57,
    "total_outputs": 150,
    "selection": "Three intentionally selected changed examples; includes a failure, not a representative quality estimate."
  },
  "samples": [
    {
      "sample_id": "novel-03782e62ee9dd907a087eeac-p01s01",
      "source": "Tần Trường Sinh hiểu rất rõ, một khi mối liên hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân.",
      "candidate": "Tần Trường Sinh hiểu rất rõ, một khi mối quan hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân.",
      "changed": true,
      "generator": {
        "system_id": "visp_full",
        "raw_output": "Tần Trường Sinh hiểu rất rõ, một khi mối quan hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 3537.3416999999563
      },
      "evaluation": {
        "rank_score": 0.03741014376282692,
        "fluency_delta_proxy": 0.06693081557750702,
        "semantic_preservation_proxy": 0.8051238059997559,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.04100829362869263,
        "fluency_delta_proxy": 0.06664589047431946,
        "semantic_preservation_proxy": 0.8040511608123779,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Tần Trường Sinh hiểu rất rõ, một khi mối liên hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân.",
        "rank_margin": -0.0035981498658657074,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-03782e62ee9dd907a087eeac-p02s01",
      "source": "Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa.",
      "candidate": "Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa.",
      "changed": false,
      "generator": {
        "system_id": "visp_full",
        "raw_output": "Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 2429.046499999913
      },
      "evaluation": {
        "rank_score": -0.3314342796802521,
        "fluency_delta_proxy": 0.06568527221679688,
        "semantic_preservation_proxy": 0.8544645309448242,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": -0.3314342796802521,
        "fluency_delta_proxy": 0.06568527221679688,
        "semantic_preservation_proxy": 0.8544645309448242,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa.",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-03782e62ee9dd907a087eeac-p03s01",
      "source": "Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: \"Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!\"",
      "candidate": "Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: \"Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!\"",
      "changed": false,
      "generator": {
        "system_id": "visp_full",
        "raw_output": "Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: \"Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!\"",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 3916.641800000093
      },
      "evaluation": {
        "rank_score": 0.17851196229457855,
        "fluency_delta_proxy": 0.061544544994831085,
        "semantic_preservation_proxy": 0.5856443643569946,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.17851196229457855,
        "fluency_delta_proxy": 0.061544544994831085,
        "semantic_preservation_proxy": 0.5856443643569946,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: \"Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!\"",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-11951127ca879f416798c2df-p03s01",
      "source": "Chỉ là Tần Trường Sinh vốn không có ý định bán linh mễ.",
      "candidate": "Tần Trường Sinh vốn không có ý định bán linh mễ.",
      "generator": {
        "sample_id": "novel-11951127ca879f416798c2df-p03s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Tần Trường Sinh vốn không có ý định bán linh mễ.",
        "output_vi": "Tần Trường Sinh vốn không có ý định bán linh mễ.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 548.0811950000088
      },
      "inspection_note": "Bỏ cụm “Chỉ là”. Có thay đổi, nhưng cần ngữ cảnh để quyết định có nên bỏ từ nối hay không.",
      "evaluation": {
        "rank_score": -0.46466830372810364,
        "fluency_delta_proxy": 0.07201917469501495,
        "semantic_preservation_proxy": 0.8061755895614624,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "evaluation_status": "scored_with_identity_comparison",
      "identity_comparison": {
        "rank_score": -0.3648703694343567,
        "fluency_delta_proxy": 0.06654292345046997,
        "semantic_preservation_proxy": 0.7973923087120056,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Chỉ là Tần Trường Sinh vốn không có ý định bán linh mễ.",
        "rank_margin": -0.09979793429374695,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint"
    },
    {
      "sample_id": "novel-78d36c59db8687a5aa2854ef-p09s01",
      "source": "Hơn nữa Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần.",
      "candidate": "Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần.",
      "generator": {
        "sample_id": "novel-78d36c59db8687a5aa2854ef-p09s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần.",
        "output_vi": "Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 277.1247640000638
      },
      "inspection_note": "Bỏ cụm “Hơn nữa”. Đây là rút gọn từ nối, chưa chứng minh câu tốt hơn.",
      "evaluation": {
        "rank_score": -0.42837584018707275,
        "fluency_delta_proxy": 0.06637215614318848,
        "semantic_preservation_proxy": 0.7760633826255798,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "evaluation_status": "scored_with_identity_comparison",
      "identity_comparison": {
        "rank_score": -0.37272894382476807,
        "fluency_delta_proxy": 0.06384243071079254,
        "semantic_preservation_proxy": 0.7628244757652283,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Hơn nữa Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần.",
        "rank_margin": -0.05564689636230469,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint"
    },
    {
      "sample_id": "novel-34ba277e8c6f44f9c5601bd0-p07s01",
      "source": "Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, muốn thu thập về tặng cho mẹ, nên mới lên tiếng.",
      "candidate": "Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, nên mới lên tiếng.",
      "generator": {
        "sample_id": "novel-34ba277e8c6f44f9c5601bd0-p07s01",
        "work_id": "huyen-huyen-nu-nhi-roi-nui-ta-dai-de-than-phan-tang-khong-duoc",
        "system_id": "visp_full",
        "raw_output": "Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, nên mới lên tiếng.",
        "output_vi": "Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, nên mới lên tiếng.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 515.8993569999666
      },
      "inspection_note": "LỖI MẤT Ý: bỏ mục đích “muốn thu thập về tặng cho mẹ”. Không nên chấp nhận output này.",
      "evaluation": {
        "rank_score": -0.523073136806488,
        "fluency_delta_proxy": 0.07577069848775864,
        "semantic_preservation_proxy": 0.8722171187400818,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "evaluation_status": "scored_with_identity_comparison",
      "identity_comparison": {
        "rank_score": -0.29205816984176636,
        "fluency_delta_proxy": 0.06279334425926208,
        "semantic_preservation_proxy": 0.8598604798316956,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "rank_margin_deleted_minus_identity": -0.23101472854614258,
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, muốn thu thập về tặng cho mẹ, nên mới lên tiếng.",
        "rank_margin": -0.23101496696472168,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      }
    },
    {
      "sample_id": "novel-a1ee2c2cabef85305b75007c-p05s01",
      "source": "Chàng vô thức đưa tay cầm lấy một lá, cảm nhận được hơi ấm và linh khí quen thuộc, lại lật xem bốn lá còn lại, tất cả đều là Hỏa Đạn Phù thành phẩm thực thụ, tuyệt đối không phải ảo giác.",
      "candidate": "Chàng vô thức đưa tay cầm lấy một lá, cảm nhận được hơi ấm và linh khí quen thuộc, lại lật xem bốn lá còn lại.",
      "generator": {
        "sample_id": "novel-a1ee2c2cabef85305b75007c-p05s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Chàng vô thức đưa tay cầm lấy một lá, cảm nhận được hơi ấm và linh khí quen thuộc, lại lật xem bốn lá còn lại.",
        "output_vi": "Chàng vô thức đưa tay cầm lấy một lá, cảm nhận được hơi ấm và linh khí quen thuộc, lại lật xem bốn lá còn lại.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 838.8864680000552
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.6466372609138489,
        "fluency_delta_proxy": 0.11212238669395447,
        "semantic_preservation_proxy": 0.9067639708518982,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.12169407308101654,
        "fluency_delta_proxy": 0.062392719089984894,
        "semantic_preservation_proxy": 0.716701090335846,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Chàng vô thức đưa tay cầm lấy một lá, cảm nhận được hơi ấm và linh khí quen thuộc, lại lật xem bốn lá còn lại, tất cả đều là Hỏa Đạn Phù thành phẩm thực thụ, tuyệt đối không phải ảo giác.",
        "rank_margin": -0.7683313339948654,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-8c6b0eb46bc8b4ab18d5f221-p08s01",
      "source": "Trong sách ghi chép, Ma Yêu là một loại yêu quái, là dã thú sau khi ăn phải máu thịt của người hoặc vật nhiễm phải thứ quỷ dị, bị luồng sức mạnh đó làm cho biến dị mà thành!",
      "candidate": "Ma Yêu là một loại yêu quái, là dã thú sau khi ăn phải máu thịt của người hoặc vật nhiễm phải thứ quỷ dị, bị luồng sức mạnh đó làm cho biến dị mà thành!",
      "generator": {
        "sample_id": "novel-8c6b0eb46bc8b4ab18d5f221-p08s01",
        "work_id": "vo-dich-tieu-nguoi-khai-cuc-ho-tong-diet-the-de-nu",
        "system_id": "visp_full",
        "raw_output": "Ma Yêu là một loại yêu quái, là dã thú sau khi ăn phải máu thịt của người hoặc vật nhiễm phải thứ quỷ dị, bị luồng sức mạnh đó làm cho biến dị mà thành!",
        "output_vi": "Ma Yêu là một loại yêu quái, là dã thú sau khi ăn phải máu thịt của người hoặc vật nhiễm phải thứ quỷ dị, bị luồng sức mạnh đó làm cho biến dị mà thành!",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 774.1428240000232
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.12367759644985199,
        "fluency_delta_proxy": 0.06660476326942444,
        "semantic_preservation_proxy": 0.637908399105072,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.1677224189043045,
        "fluency_delta_proxy": 0.06218410283327103,
        "semantic_preservation_proxy": 0.6150358319282532,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.19185235625002406,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Trong sách ghi chép, Ma Yêu là một loại yêu quái, là dã thú sau khi ăn phải máu thịt của người hoặc vật nhiễm phải thứ quỷ dị, bị luồng sức mạnh đó làm cho biến dị mà thành!",
        "rank_margin": -0.044044822454452515,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-b17ed12a76df7b3e359532f2-p06s01",
      "source": "Vương Tùng bước lên trước một bước, lập tức chắp tay với Trần Quan: “Tiêu sư Trần, dọc đường vất vả rồi, mau mau mời vào!”",
      "candidate": "Vương Tùng bước lên trước một bước, chắp tay với Trần Quan: Tiêu sư Trần, dọc đường vất vả rồi, mau mau mời vào!",
      "generator": {
        "sample_id": "novel-b17ed12a76df7b3e359532f2-p06s01",
        "work_id": "vo-dich-tieu-nguoi-khai-cuc-ho-tong-diet-the-de-nu",
        "system_id": "visp_full",
        "raw_output": "Vương Tùng bước lên trước một bước, chắp tay với Trần Quan: Tiêu sư Trần, dọc đường vất vả rồi, mau mau mời vào!",
        "output_vi": "Vương Tùng bước lên trước một bước, chắp tay với Trần Quan: Tiêu sư Trần, dọc đường vất vả rồi, mau mau mời vào!",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 633.262736000006
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.10212196409702301,
        "fluency_delta_proxy": 0.06817395240068436,
        "semantic_preservation_proxy": 0.6523858904838562,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.1684705913066864,
        "fluency_delta_proxy": 0.062105558812618256,
        "semantic_preservation_proxy": 0.6164573431015015,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Vương Tùng bước lên trước một bước, lập tức chắp tay với Trần Quan: “Tiêu sư Trần, dọc đường vất vả rồi, mau mau mời vào!”",
        "rank_margin": -0.06634862720966339,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-a1ee2c2cabef85305b75007c-p01s01",
      "source": "Khi nét bút cuối cùng hạ xuống, mặt giấy bùa đột nhiên bừng lên một tầng hồng quang ấm áp, linh khí dao động bỗng chốc ngưng tụ, một lá Hỏa Đạn Phù hoàn chỉnh vững vàng rơi xuống mặt bàn, thân bùa hơi nóng lên, toả ra khí tức tấn công đầy nội liễm.",
      "candidate": "Khi nét bút cuối cùng hạ xuống, mặt giấy bùa bỗng bừng lên một tầng hồng quang ấm áp, linh khí dao động bỗng chốc ngưng tụ, một lá Hỏa Đạn Phù hoàn chỉnh vững vàng rơi xuống mặt bàn, thân bùa hơi nóng lên, tỏa ra khí tức tấn công đầy nội liễm.",
      "generator": {
        "sample_id": "novel-a1ee2c2cabef85305b75007c-p01s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Khi nét bút cuối cùng hạ xuống, mặt giấy bùa bỗng bừng lên một tầng hồng quang ấm áp, linh khí dao động bỗng chốc ngưng tụ, một lá Hỏa Đạn Phù hoàn chỉnh vững vàng rơi xuống mặt bàn, thân bùa hơi nóng lên, tỏa ra khí tức tấn công đầy nội liễm.",
        "output_vi": "Khi nét bút cuối cùng hạ xuống, mặt giấy bùa bỗng bừng lên một tầng hồng quang ấm áp, linh khí dao động bỗng chốc ngưng tụ, một lá Hỏa Đạn Phù hoàn chỉnh vững vàng rơi xuống mặt bàn, thân bùa hơi nóng lên, tỏa ra khí tức tấn công đầy nội liễm.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 1068.2844780000096
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.16040809452533722,
        "fluency_delta_proxy": 0.06167903169989586,
        "semantic_preservation_proxy": 0.6218123435974121,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.1668177992105484,
        "fluency_delta_proxy": 0.06112015247344971,
        "semantic_preservation_proxy": 0.6161145567893982,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Khi nét bút cuối cùng hạ xuống, mặt giấy bùa đột nhiên bừng lên một tầng hồng quang ấm áp, linh khí dao động bỗng chốc ngưng tụ, một lá Hỏa Đạn Phù hoàn chỉnh vững vàng rơi xuống mặt bàn, thân bùa hơi nóng lên, toả ra khí tức tấn công đầy nội liễm.",
        "rank_margin": -0.006409704685211182,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-11951127ca879f416798c2df-p11s01",
      "source": "Tần Trường Sinh giả vờ nghi hoặc hỏi: \"Các hạ là?\"",
      "candidate": "Tần Trường Sinh giả vờ nghi hoặc hỏi: \"Các hạ là ai?\"",
      "generator": {
        "sample_id": "novel-11951127ca879f416798c2df-p11s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Tần Trường Sinh giả vờ nghi hoặc hỏi: \"Các hạ là ai?\"",
        "output_vi": "Tần Trường Sinh giả vờ nghi hoặc hỏi: \"Các hạ là ai?\"",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 325.5262019999918
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.035146817564964294,
        "fluency_delta_proxy": 0.06710471212863922,
        "semantic_preservation_proxy": 0.7622484564781189,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.058284856379032135,
        "fluency_delta_proxy": 0.06498768925666809,
        "semantic_preservation_proxy": 0.7496970891952515,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Tần Trường Sinh giả vờ nghi hoặc hỏi: \"Các hạ là?\"",
        "rank_margin": -0.02313803881406784,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-03782e62ee9dd907a087eeac-p04s01",
      "source": "Trương Viễn nghe theo lời Tần Trường Sinh, thay lên y phục của đệ tử tạp dịch.",
      "candidate": "Trương Viễn nghe theo lời Tần Trường Sinh, thay y phục của đệ tử tạp dịch.",
      "generator": {
        "sample_id": "novel-03782e62ee9dd907a087eeac-p04s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Trương Viễn nghe theo lời Tần Trường Sinh, thay y phục của đệ tử tạp dịch.",
        "output_vi": "Trương Viễn nghe theo lời Tần Trường Sinh, thay y phục của đệ tử tạp dịch.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 350.61351100000593
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.3920290470123291,
        "fluency_delta_proxy": 0.06421168148517609,
        "semantic_preservation_proxy": 0.7821088433265686,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": -0.37413454055786133,
        "fluency_delta_proxy": 0.06227126717567444,
        "semantic_preservation_proxy": 0.7663692831993103,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Trương Viễn nghe theo lời Tần Trường Sinh, thay lên y phục của đệ tử tạp dịch.",
        "rank_margin": -0.017894506454467773,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-78d36c59db8687a5aa2854ef-p01s01",
      "source": "Mà sự tiến bộ trên con đường chế phù, càng khiến chính Tần Trường Sinh cũng phải kinh ngạc không thôi.",
      "candidate": "Mà sự tiến bộ trên con đường chế phù, càng khiến chính Tần Trường Sinh phải kinh ngạc không thôi.",
      "generator": {
        "sample_id": "novel-78d36c59db8687a5aa2854ef-p01s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Mà sự tiến bộ trên con đường chế phù, càng khiến chính Tần Trường Sinh phải kinh ngạc không thôi.",
        "output_vi": "Mà sự tiến bộ trên con đường chế phù, càng khiến chính Tần Trường Sinh phải kinh ngạc không thôi.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 419.16470299997854
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.3972107172012329,
        "fluency_delta_proxy": 0.07743875682353973,
        "semantic_preservation_proxy": 0.8956350684165955,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": -0.24421453475952148,
        "fluency_delta_proxy": 0.06891617923974991,
        "semantic_preservation_proxy": 0.883798360824585,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Mà sự tiến bộ trên con đường chế phù, càng khiến chính Tần Trường Sinh cũng phải kinh ngạc không thôi.",
        "rank_margin": -0.15299618244171143,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-979489eb99fe8cd867305268-p12s01",
      "source": "Hắn còn chưa kịp thốt ra một tiếng kêu thảm, máu tươi đã trào ra từ miệng và mũi, mất sạch khả năng chiến đấu.",
      "candidate": "Hắn còn chưa kịp thốt ra một tiếng kêu thảm, máu tươi đã trào ra từ miệng và mũi, mất hết khả năng chiến đấu.",
      "generator": {
        "sample_id": "novel-979489eb99fe8cd867305268-p12s01",
        "work_id": "vo-dich-tieu-nguoi-khai-cuc-ho-tong-diet-the-de-nu",
        "system_id": "visp_full",
        "raw_output": "Hắn còn chưa kịp thốt ra một tiếng kêu thảm, máu tươi đã trào ra từ miệng và mũi, mất hết khả năng chiến đấu.",
        "output_vi": "Hắn còn chưa kịp thốt ra một tiếng kêu thảm, máu tươi đã trào ra từ miệng và mũi, mất hết khả năng chiến đấu.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 539.293354999927
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.2124684453010559,
        "fluency_delta_proxy": 0.07063508033752441,
        "semantic_preservation_proxy": 0.8868797421455383,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": -0.2018946260213852,
        "fluency_delta_proxy": 0.06899300217628479,
        "semantic_preservation_proxy": 0.881405770778656,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Hắn còn chưa kịp thốt ra một tiếng kêu thảm, máu tươi đã trào ra từ miệng và mũi, mất sạch khả năng chiến đấu.",
        "rank_margin": -0.010573819279670715,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-03782e62ee9dd907a087eeac-p08s02",
      "source": "Khi bán cố gắng tránh người quen, nếu cần giao dịch thì chỉ bàn chuyện làm ăn, không nên tán gẫu nhiều.\"",
      "candidate": "Khi bán cố gắng tránh xa người quen, nếu cần giao dịch thì chỉ bàn chuyện làm ăn, không nên tán gẫu nhiều.",
      "generator": {
        "sample_id": "novel-03782e62ee9dd907a087eeac-p08s02",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Khi bán cố gắng tránh xa người quen, nếu cần giao dịch thì chỉ bàn chuyện làm ăn, không nên tán gẫu nhiều.",
        "output_vi": "Khi bán cố gắng tránh xa người quen, nếu cần giao dịch thì chỉ bàn chuyện làm ăn, không nên tán gẫu nhiều.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 504.9132289999534
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.6453213095664978,
        "fluency_delta_proxy": 0.11655561625957489,
        "semantic_preservation_proxy": 0.9052565693855286,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.13854806125164032,
        "fluency_delta_proxy": 0.0632609874010086,
        "semantic_preservation_proxy": 0.6830965280532837,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Khi bán cố gắng tránh người quen, nếu cần giao dịch thì chỉ bàn chuyện làm ăn, không nên tán gẫu nhiều.\"",
        "rank_margin": -0.7838693708181381,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-3c33128b146ff937dbce0545-p09s01",
      "source": "“Các huynh nói nơi thi đấu sẽ có rất nhiều hoa đẹp là thật sao?”",
      "candidate": "Các huynh nói nơi thi đấu sẽ có rất nhiều hoa đẹp là thật sao?",
      "generator": {
        "sample_id": "novel-3c33128b146ff937dbce0545-p09s01",
        "work_id": "huyen-huyen-nu-nhi-roi-nui-ta-dai-de-than-phan-tang-khong-duoc",
        "system_id": "visp_full",
        "raw_output": "Các huynh nói nơi thi đấu sẽ có rất nhiều hoa đẹp là thật sao?",
        "output_vi": "Các huynh nói nơi thi đấu sẽ có rất nhiều hoa đẹp là thật sao?",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 365.8834869999055
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.7119997143745422,
        "fluency_delta_proxy": 0.1219034194946289,
        "semantic_preservation_proxy": 0.8805291652679443,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.1665468066930771,
        "fluency_delta_proxy": 0.06216060370206833,
        "semantic_preservation_proxy": 0.61150062084198,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.056294018750008945,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "“Các huynh nói nơi thi đấu sẽ có rất nhiều hoa đẹp là thật sao?”",
        "rank_margin": -0.8785465210676193,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-979489eb99fe8cd867305268-p19s02",
      "source": "Trả thù cho lão Lưu, lão Vương đi!!”",
      "candidate": "Trả thù cho lão Lưu, lão Vương đi!!",
      "generator": {
        "sample_id": "novel-979489eb99fe8cd867305268-p19s02",
        "work_id": "vo-dich-tieu-nguoi-khai-cuc-ho-tong-diet-the-de-nu",
        "system_id": "visp_full",
        "raw_output": "Trả thù cho lão Lưu, lão Vương đi!!",
        "output_vi": "Trả thù cho lão Lưu, lão Vương đi!!",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 236.0545239999965
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.12758024036884308,
        "fluency_delta_proxy": 0.08673971891403198,
        "semantic_preservation_proxy": 0.7869298458099365,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.08156488835811615,
        "fluency_delta_proxy": 0.06871560215950012,
        "semantic_preservation_proxy": 0.723246157169342,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Trả thù cho lão Lưu, lão Vương đi!!”",
        "rank_margin": -0.20914512872695923,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-3c33128b146ff937dbce0545-p05s01",
      "source": "“Nàng Nàng, sắp đến lúc con tham gia thi đấu rồi, sao con chẳng sốt ruột chút nào vậy!”",
      "candidate": "Nàng Nàng, sắp đến lúc con tham gia thi đấu rồi, sao con chẳng sốt ruột chút nào vậy!",
      "generator": {
        "sample_id": "novel-3c33128b146ff937dbce0545-p05s01",
        "work_id": "huyen-huyen-nu-nhi-roi-nui-ta-dai-de-than-phan-tang-khong-duoc",
        "system_id": "visp_full",
        "raw_output": "Nàng Nàng, sắp đến lúc con tham gia thi đấu rồi, sao con chẳng sốt ruột chút nào vậy!",
        "output_vi": "Nàng Nàng, sắp đến lúc con tham gia thi đấu rồi, sao con chẳng sốt ruột chút nào vậy!",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 485.2184110000053
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.050883252173662186,
        "fluency_delta_proxy": 0.07421799004077911,
        "semantic_preservation_proxy": 0.6699788570404053,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.17818455398082733,
        "fluency_delta_proxy": 0.06184966862201691,
        "semantic_preservation_proxy": 0.5893235802650452,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "“Nàng Nàng, sắp đến lúc con tham gia thi đấu rồi, sao con chẳng sốt ruột chút nào vậy!”",
        "rank_margin": -0.12730130180716515,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-699100c90e795ceed38b3f2c-p04s02",
      "source": "Lưu Na trực tiếp đánh người ta tàn phế luôn đó.”",
      "candidate": "Lưu Na trực tiếp đánh người ta tàn phế luôn đó.",
      "generator": {
        "sample_id": "novel-699100c90e795ceed38b3f2c-p04s02",
        "work_id": "huyen-huyen-nu-nhi-roi-nui-ta-dai-de-than-phan-tang-khong-duoc",
        "system_id": "visp_full",
        "raw_output": "Lưu Na trực tiếp đánh người ta tàn phế luôn đó.",
        "output_vi": "Lưu Na trực tiếp đánh người ta tàn phế luôn đó.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 246.99117499994827
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.912899911403656,
        "fluency_delta_proxy": 0.12417003512382507,
        "semantic_preservation_proxy": 0.9116323590278625,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.010740767233073711,
        "fluency_delta_proxy": 0.06773534417152405,
        "semantic_preservation_proxy": 0.7995259165763855,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Lưu Na trực tiếp đánh người ta tàn phế luôn đó.”",
        "rank_margin": -0.9236406786367297,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-af0c2d2df1572c54de323bcc-p09s01",
      "source": "Nghe vậy, Lâm Hạo Phàm chỉ đành cười khổ lắc đầu: “Đợi con đột phá cảnh giới Thánh Hoàng thì cha mới có thể dẫn Niệm Niệm đi được, nếu không mẹ sẽ giận đó, Niệm Niệm đợi thêm chút nữa có được không.”",
      "candidate": "Nghe vậy, Lâm Hạo Phàm chỉ đành cười khổ lắc đầu: Đợi con đột phá cảnh giới Thánh Hoàng thì cha mới có thể dẫn Niệm Niệm đi được, nếu không mẹ sẽ giận đó, Niệm Niệm đợi thêm chút nữa có được không?",
      "generator": {
        "sample_id": "novel-af0c2d2df1572c54de323bcc-p09s01",
        "work_id": "huyen-huyen-nu-nhi-roi-nui-ta-dai-de-than-phan-tang-khong-duoc",
        "system_id": "visp_full",
        "raw_output": "Nghe vậy, Lâm Hạo Phàm chỉ đành cười khổ lắc đầu: Đợi con đột phá cảnh giới Thánh Hoàng thì cha mới có thể dẫn Niệm Niệm đi được, nếu không mẹ sẽ giận đó, Niệm Niệm đợi thêm chút nữa có được không?",
        "output_vi": "Nghe vậy, Lâm Hạo Phàm chỉ đành cười khổ lắc đầu: Đợi con đột phá cảnh giới Thánh Hoàng thì cha mới có thể dẫn Niệm Niệm đi được, nếu không mẹ sẽ giận đó, Niệm Niệm đợi thêm chút nữa có được không?",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 913.8361139999915
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.08141939342021942,
        "fluency_delta_proxy": 0.06820383667945862,
        "semantic_preservation_proxy": 0.6455134749412537,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.1824084222316742,
        "fluency_delta_proxy": 0.06013438105583191,
        "semantic_preservation_proxy": 0.5840755701065063,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Nghe vậy, Lâm Hạo Phàm chỉ đành cười khổ lắc đầu: “Đợi con đột phá cảnh giới Thánh Hoàng thì cha mới có thể dẫn Niệm Niệm đi được, nếu không mẹ sẽ giận đó, Niệm Niệm đợi thêm chút nữa có được không.”",
        "rank_margin": -0.10098902881145477,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-b17ed12a76df7b3e359532f2-p01s02",
      "source": "Một tên thuộc hạ bên cạnh hắn cũng tặc lưỡi kinh ngạc, “Đây chính là người duy nhất sống sót đi đến dưới chân thành Vọng Nguyệt trong suốt nửa tháng qua!”",
      "candidate": "Một tên thuộc hạ bên cạnh hắn cũng tặc lưỡi kinh ngạc, Đây chính là người duy nhất sống sót đi đến dưới chân thành Vọng Nguyệt trong suốt nửa tháng qua!",
      "generator": {
        "sample_id": "novel-b17ed12a76df7b3e359532f2-p01s02",
        "work_id": "vo-dich-tieu-nguoi-khai-cuc-ho-tong-diet-the-de-nu",
        "system_id": "visp_full",
        "raw_output": "Một tên thuộc hạ bên cạnh hắn cũng tặc lưỡi kinh ngạc, Đây chính là người duy nhất sống sót đi đến dưới chân thành Vọng Nguyệt trong suốt nửa tháng qua!",
        "output_vi": "Một tên thuộc hạ bên cạnh hắn cũng tặc lưỡi kinh ngạc, Đây chính là người duy nhất sống sót đi đến dưới chân thành Vọng Nguyệt trong suốt nửa tháng qua!",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 680.4027050000059
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.12007899582386017,
        "fluency_delta_proxy": 0.06770946085453033,
        "semantic_preservation_proxy": 0.6207185983657837,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.18247421085834503,
        "fluency_delta_proxy": 0.06172648444771767,
        "semantic_preservation_proxy": 0.5805277824401855,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Một tên thuộc hạ bên cạnh hắn cũng tặc lưỡi kinh ngạc, “Đây chính là người duy nhất sống sót đi đến dưới chân thành Vọng Nguyệt trong suốt nửa tháng qua!”",
        "rank_margin": -0.06239521503448486,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-a1ee2c2cabef85305b75007c-p03s01",
      "source": "Trên bàn vốn chỉ có một lá Hỏa Đạn Phù, vậy mà với tốc độ mắt thường có thể thấy được, nó tự phân tách ra thêm bốn lá bùa y hệt, cộng với lá ban đầu, năm lá Hỏa Đạn Phù xếp chồng ngay ngắn lên nhau, hồng quang và linh khí dao động của mỗi lá đều không sai biệt chút nào, phẩm chất hoàn toàn đồng nhất.",
      "candidate": "Trên bàn vốn chỉ có một lá Hỏa Đạn Phù, vậy mà với tốc độ mắt thường có thể thấy được, nó tự phân tách thêm bốn lá bùa y hệt, cộng với lá ban đầu, năm lá Hỏa Đạn Phù xếp chồng ngay ngắn lên nhau, hồng quang và linh khí dao động của mỗi lá đều không sai biệt chút nào, phẩm chất hoàn toàn đồng nhất.",
      "generator": {
        "sample_id": "novel-a1ee2c2cabef85305b75007c-p03s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Trên bàn vốn chỉ có một lá Hỏa Đạn Phù, vậy mà với tốc độ mắt thường có thể thấy được, nó tự phân tách thêm bốn lá bùa y hệt, cộng với lá ban đầu, năm lá Hỏa Đạn Phù xếp chồng ngay ngắn lên nhau, hồng quang và linh khí dao động của mỗi lá đều không sai biệt chút nào, phẩm chất hoàn toàn đồng nhất.",
        "output_vi": "Trên bàn vốn chỉ có một lá Hỏa Đạn Phù, vậy mà với tốc độ mắt thường có thể thấy được, nó tự phân tách thêm bốn lá bùa y hệt, cộng với lá ban đầu, năm lá Hỏa Đạn Phù xếp chồng ngay ngắn lên nhau, hồng quang và linh khí dao động của mỗi lá đều không sai biệt chút nào, phẩm chất hoàn toàn đồng nhất.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 1325.520818999962
      },
      "inspection_note": "Có khác biệt văn bản; phần gạch ngang/in đậm chỉ thể hiện khác biệt ký tự/từ, không xác nhận cải thiện hoặc giữ nghĩa.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.15863968431949615,
        "fluency_delta_proxy": 0.06213704124093056,
        "semantic_preservation_proxy": 0.6276530027389526,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.1656888723373413,
        "fluency_delta_proxy": 0.06145498901605606,
        "semantic_preservation_proxy": 0.6213901042938232,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Điểm xếp hạng phương án thấp hơn hoặc bằng câu gốc; đồng thời không vượt ngưỡng gate.",
        "selected_text": "Trên bàn vốn chỉ có một lá Hỏa Đạn Phù, vậy mà với tốc độ mắt thường có thể thấy được, nó tự phân tách ra thêm bốn lá bùa y hệt, cộng với lá ban đầu, năm lá Hỏa Đạn Phù xếp chồng ngay ngắn lên nhau, hồng quang và linh khí dao động của mỗi lá đều không sai biệt chút nào, phẩm chất hoàn toàn đồng nhất.",
        "rank_margin": -0.007049188017845154,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-03782e62ee9dd907a087eeac-p05s01",
      "source": "\"Nhiệm vụ hàng đầu của ngươi là đến phường thị bán Hỏa Đạn Phù.\"",
      "candidate": "\"Nhiệm vụ hàng đầu của ngươi là đến phường thị bán Hỏa Đạn Phù.\"",
      "generator": {
        "sample_id": "novel-03782e62ee9dd907a087eeac-p05s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "\"Nhiệm vụ hàng đầu của ngươi là đến phường thị bán Hỏa Đạn Phù.\"",
        "output_vi": "\"Nhiệm vụ hàng đầu của ngươi là đến phường thị bán Hỏa Đạn Phù.\"",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 339.46948900006646
      },
      "inspection_note": "Output trùng câu gốc; không có sửa đổi để áp dụng.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.15127451717853546,
        "fluency_delta_proxy": 0.06307336688041687,
        "semantic_preservation_proxy": 0.6363766193389893,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.15127451717853546,
        "fluency_delta_proxy": 0.06307336688041687,
        "semantic_preservation_proxy": 0.6363766193389893,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "\"Nhiệm vụ hàng đầu của ngươi là đến phường thị bán Hỏa Đạn Phù.\"",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-11951127ca879f416798c2df-p13s01",
      "source": "Tần Trường Sinh trong lòng cười lạnh, tình hình cá cực tốt ư?",
      "candidate": "Tần Trường Sinh trong lòng cười lạnh, tình hình cá cực tốt ư?",
      "generator": {
        "sample_id": "novel-11951127ca879f416798c2df-p13s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Tần Trường Sinh trong lòng cười lạnh, tình hình cá cực tốt ư?",
        "output_vi": "Tần Trường Sinh trong lòng cười lạnh, tình hình cá cực tốt ư?",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 313.20322999999917
      },
      "inspection_note": "Output trùng câu gốc; không có sửa đổi để áp dụng.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.042662862688302994,
        "fluency_delta_proxy": 0.0677848681807518,
        "semantic_preservation_proxy": 0.7701922059059143,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.042662862688302994,
        "fluency_delta_proxy": 0.0677848681807518,
        "semantic_preservation_proxy": 0.7701922059059143,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.11046581250002419,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "Tần Trường Sinh trong lòng cười lạnh, tình hình cá cực tốt ư?",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-6647f48b2786a7b69e58dc09-p08s02",
      "source": "Lạc Ly bực bội lườm hắn một cái, \"Làm ta giật cả mình.\"",
      "candidate": "Lạc Ly bực bội lườm hắn một cái, \"Làm ta giật cả mình.\"",
      "generator": {
        "sample_id": "novel-6647f48b2786a7b69e58dc09-p08s02",
        "work_id": "vo-dich-tieu-nguoi-khai-cuc-ho-tong-diet-the-de-nu",
        "system_id": "visp_full",
        "raw_output": "Lạc Ly bực bội lườm hắn một cái, \"Làm ta giật cả mình.\"",
        "output_vi": "Lạc Ly bực bội lườm hắn một cái, \"Làm ta giật cả mình.\"",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 366.73693400007323
      },
      "inspection_note": "Output trùng câu gốc; không có sửa đổi để áp dụng.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": 0.06995798647403717,
        "fluency_delta_proxy": 0.06697410345077515,
        "semantic_preservation_proxy": 0.774025022983551,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": 0.06995798647403717,
        "fluency_delta_proxy": 0.06697410345077515,
        "semantic_preservation_proxy": 0.774025022983551,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "Lạc Ly bực bội lườm hắn một cái, \"Làm ta giật cả mình.\"",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-78d36c59db8687a5aa2854ef-p04s01",
      "source": "Điều quý giá hơn là, bùa hỏa đạn ở cảnh giới đại thành có uy lực tăng hơn ba phần so với bùa chú cùng cấp.",
      "candidate": "Điều quý giá hơn là, bùa hỏa đạn ở cảnh giới đại thành có uy lực tăng hơn ba phần so với bùa chú cùng cấp.",
      "generator": {
        "sample_id": "novel-78d36c59db8687a5aa2854ef-p04s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Điều quý giá hơn là, bùa hỏa đạn ở cảnh giới đại thành có uy lực tăng hơn ba phần so với bùa chú cùng cấp.",
        "output_vi": "Điều quý giá hơn là, bùa hỏa đạn ở cảnh giới đại thành có uy lực tăng hơn ba phần so với bùa chú cùng cấp.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 548.5161039999866
      },
      "inspection_note": "Output trùng câu gốc; không có sửa đổi để áp dụng.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.32426565885543823,
        "fluency_delta_proxy": 0.06778638809919357,
        "semantic_preservation_proxy": 0.841440737247467,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": -0.32426565885543823,
        "fluency_delta_proxy": 0.06778638809919357,
        "semantic_preservation_proxy": 0.841440737247467,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "Điều quý giá hơn là, bùa hỏa đạn ở cảnh giới đại thành có uy lực tăng hơn ba phần so với bùa chú cùng cấp.",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-8c6b0eb46bc8b4ab18d5f221-p12s01",
      "source": "Con ma sói ngửi thấy mùi máu thịt của người và ngựa phía trước, đôi mắt đỏ ngầu lập tức ánh lên vẻ tham lam.",
      "candidate": "Con ma sói ngửi thấy mùi máu thịt của người và ngựa phía trước, đôi mắt đỏ ngầu lập tức ánh lên vẻ tham lam.",
      "generator": {
        "sample_id": "novel-8c6b0eb46bc8b4ab18d5f221-p12s01",
        "work_id": "vo-dich-tieu-nguoi-khai-cuc-ho-tong-diet-the-de-nu",
        "system_id": "visp_full",
        "raw_output": "Con ma sói ngửi thấy mùi máu thịt của người và ngựa phía trước, đôi mắt đỏ ngầu lập tức ánh lên vẻ tham lam.",
        "output_vi": "Con ma sói ngửi thấy mùi máu thịt của người và ngựa phía trước, đôi mắt đỏ ngầu lập tức ánh lên vẻ tham lam.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 490.25526200000513
      },
      "inspection_note": "Output trùng câu gốc; không có sửa đổi để áp dụng.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.3461756110191345,
        "fluency_delta_proxy": 0.06125124916434288,
        "semantic_preservation_proxy": 0.8257377743721008,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": -0.3461756110191345,
        "fluency_delta_proxy": 0.06125124916434288,
        "semantic_preservation_proxy": 0.8257377743721008,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "Con ma sói ngửi thấy mùi máu thịt của người và ngựa phía trước, đôi mắt đỏ ngầu lập tức ánh lên vẻ tham lam.",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-af0c2d2df1572c54de323bcc-p13s02",
      "source": "Lâm Hạo Phàm xoa đầu con gái ngoan an ủi.",
      "candidate": "Lâm Hạo Phàm xoa đầu con gái ngoan an ủi.",
      "generator": {
        "sample_id": "novel-af0c2d2df1572c54de323bcc-p13s02",
        "work_id": "huyen-huyen-nu-nhi-roi-nui-ta-dai-de-than-phan-tang-khong-duoc",
        "system_id": "visp_full",
        "raw_output": "Lâm Hạo Phàm xoa đầu con gái ngoan an ủi.",
        "output_vi": "Lâm Hạo Phàm xoa đầu con gái ngoan an ủi.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 247.47360100002425
      },
      "inspection_note": "Output trùng câu gốc; không có sửa đổi để áp dụng.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.36555802822113037,
        "fluency_delta_proxy": 0.0632224977016449,
        "semantic_preservation_proxy": 0.7712017297744751,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": -0.36555802822113037,
        "fluency_delta_proxy": 0.0632224977016449,
        "semantic_preservation_proxy": 0.7712017297744751,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "Lâm Hạo Phàm xoa đầu con gái ngoan an ủi.",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-bdc44dab6d59719d51c7c048-p11s01",
      "source": "Tần Trường Sinh hít sâu một hơi, cúi người vung liềm.",
      "candidate": "Tần Trường Sinh hít sâu một hơi, cúi người vung liềm.",
      "generator": {
        "sample_id": "novel-bdc44dab6d59719d51c7c048-p11s01",
        "work_id": "tu-tien-mot-nam-mot-muc-tu-ta-vo-dich",
        "system_id": "visp_full",
        "raw_output": "Tần Trường Sinh hít sâu một hơi, cúi người vung liềm.",
        "output_vi": "Tần Trường Sinh hít sâu một hơi, cúi người vung liềm.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 246.8897910000578
      },
      "inspection_note": "Output trùng câu gốc; không có sửa đổi để áp dụng.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.3675323724746704,
        "fluency_delta_proxy": 0.06465911120176315,
        "semantic_preservation_proxy": 0.807771623134613,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": -0.3675323724746704,
        "fluency_delta_proxy": 0.06465911120176315,
        "semantic_preservation_proxy": 0.807771623134613,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "Tần Trường Sinh hít sâu một hơi, cúi người vung liềm.",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    },
    {
      "sample_id": "novel-d7f9895034b4cf2b9f3f584d-p15s01",
      "source": "Kết quả là thứ mà mình tự hào, trong mắt kẻ địch lại chỉ là rác rưởi.",
      "candidate": "Kết quả là thứ mà mình tự hào, trong mắt kẻ địch lại chỉ là rác rưởi.",
      "generator": {
        "sample_id": "novel-d7f9895034b4cf2b9f3f584d-p15s01",
        "work_id": "huyen-huyen-nu-nhi-roi-nui-ta-dai-de-than-phan-tang-khong-duoc",
        "system_id": "visp_full",
        "raw_output": "Kết quả là thứ mà mình tự hào, trong mắt kẻ địch lại chỉ là rác rưởi.",
        "output_vi": "Kết quả là thứ mà mình tự hào, trong mắt kẻ địch lại chỉ là rác rưởi.",
        "status": "ok",
        "fallback": false,
        "error": null,
        "latency_ms": 357.49609799995596
      },
      "inspection_note": "Output trùng câu gốc; không có sửa đổi để áp dụng.",
      "source_origin": "visp_finetune/data/test.jsonl",
      "generator_output_origin": "visp_finetune/runs/test_predictions.jsonl",
      "evaluation": {
        "rank_score": -0.3598748445510864,
        "fluency_delta_proxy": 0.06642881035804749,
        "semantic_preservation_proxy": 0.7953345775604248,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "identity_comparison": {
        "rank_score": -0.3598748445510864,
        "fluency_delta_proxy": 0.06642881035804749,
        "semantic_preservation_proxy": 0.7953345775604248,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.02049200000010387,
        "latency_scope": "model_forward_excludes_tokenization"
      },
      "decision": {
        "action": "keep_original",
        "decision_vi": "Giữ câu gốc",
        "reason_vi": "Phương án ViSP trùng câu gốc, không có chỉnh sửa để áp dụng.",
        "selected_text": "Kết quả là thứ mà mình tự hào, trong mắt kẻ địch lại chỉ là rác rưởi.",
        "rank_margin": 0.0,
        "gate_threshold": 1000000000.0,
        "decision_origin": "deterministic_rank_margin_gate",
        "not_a_model_generated_semantic_explanation": true
      },
      "evaluation_origin": "Published handoff ZIP checkpoint",
      "evaluation_status": "scored_with_identity_comparison"
    }
  ],
  "sample_selection": {
    "total": 30,
    "changed": 20,
    "unchanged": 10,
    "method": "Preserve initial six; add historical outputs distributed across edit-similarity range.",
    "representative_quality_estimate": false
  }
}
```

</details>
