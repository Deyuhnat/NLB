# Sample output chung — ViSP và evaluator

Đây là **output đã chạy thật**, không chỉnh sửa câu model trả về. Có ví dụ giữ nguyên, sửa nhẹ và lỗi mất ý. Các ví dụ chỉ minh họa hành vi/định dạng, không phải benchmark chất lượng độc lập.

**Cách đọc:** phần bị xóa được ~~gạch ngang~~ trong câu gốc; phần thêm/thay được **in đậm** trong output. Nếu hai câu giống nhau, model đã giữ nguyên.

Trên toàn bộ test hồi cứu, ViSP thay đổi **57/150 câu (38%)**, giữ nguyên 93 câu. “Có thay đổi” không đồng nghĩa “viết lại tốt hơn”. Điểm evaluator là proxy chưa hiệu chuẩn; model hiện chưa nên làm metric chính.

[Hướng dẫn chạy và tích hợp](../README.md)

## Ví dụ 1

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Tần Trường Sinh hiểu rất rõ, một khi mối <del>liên</del> hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân. |
| Output ViSP | Tần Trường Sinh hiểu rất rõ, một khi mối <strong>quan</strong> hệ giữa hai người bị phát giác, không chỉ thân phận hóa thân bị bại lộ, mà ngay cả bí mật của bản thân hắn cũng sẽ không còn chỗ dung thân. |

**Nhận xét khi đối chiếu:** Thay “mối liên hệ” bằng “mối quan hệ”; đây là sửa nhẹ, chưa phải viết lại cấu trúc câu.

Trạng thái generator: `status=ok`, `fallback=false`.

| Điểm evaluator thực tế | Giá trị |
|---|---|
| rank_score | 0.037410 |
| fluency_delta_proxy | 0.066931 |
| semantic_preservation_proxy | 0.805124 |
| grammar_score | null |
| human_validated / context_used | false / false |

## Ví dụ 2

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa. |
| Output ViSP | Đệ tử tạp dịch qua lại đông đúc, chỉ có cắt đứt hoàn toàn liên hệ giữa bản thể và hóa thân mới có thể tránh né rủi ro ở mức tối đa. |

**Nhận xét khi đối chiếu:** Giữ nguyên câu gốc, không có thay đổi.

Trạng thái generator: `status=ok`, `fallback=false`.

| Điểm evaluator thực tế | Giá trị |
|---|---|
| rank_score | -0.331434 |
| fluency_delta_proxy | 0.065685 |
| semantic_preservation_proxy | 0.854465 |
| grammar_score | null |
| human_validated / context_used | false / false |

## Ví dụ 3

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: &quot;Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!&quot; |
| Output ViSP | Tần Trường Sinh tâm thần khẽ động, lấy ra một bộ y phục tạp dịch đã chuẩn bị sẵn đưa đến trước mặt hóa thân: &quot;Đây là y phục của ngươi, phòng của ngươi ở cách đây mười dặm về phía tây!&quot; |

**Nhận xét khi đối chiếu:** Giữ nguyên câu gốc, không có thay đổi.

Trạng thái generator: `status=ok`, `fallback=false`.

| Điểm evaluator thực tế | Giá trị |
|---|---|
| rank_score | 0.178512 |
| fluency_delta_proxy | 0.061545 |
| semantic_preservation_proxy | 0.585644 |
| grammar_score | null |
| human_validated / context_used | false / false |

## Ví dụ 4

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | <del>Chỉ là</del> Tần Trường Sinh vốn không có ý định bán linh mễ. |
| Output ViSP | Tần Trường Sinh vốn không có ý định bán linh mễ. |

**Nhận xét khi đối chiếu:** Bỏ cụm “Chỉ là”. Có thay đổi, nhưng cần ngữ cảnh để quyết định có nên bỏ từ nối hay không.

Trạng thái generator: `status=ok`, `fallback=false`.

**Evaluator:** chưa chấm riêng ví dụ này (`evaluation=null`); không có điểm giả.

## Ví dụ 5

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | <del>Hơn nữa</del> Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần. |
| Output ViSP | Tần Trường Sinh cũng đã để Vương Ngũ đến phường thị vài lần. |

**Nhận xét khi đối chiếu:** Bỏ cụm “Hơn nữa”. Đây là rút gọn từ nối, chưa chứng minh câu tốt hơn.

Trạng thái generator: `status=ok`, `fallback=false`.

**Evaluator:** chưa chấm riêng ví dụ này (`evaluation=null`); không có điểm giả.

## Ví dụ 6

| Đối chiếu | Nội dung |
|---|---|
| Câu gốc | Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, <del>muốn thu thập về tặng cho mẹ,</del> nên mới lên tiếng. |
| Output ViSP | Cô bé thấy huyết liên hoa rất đẹp, lại chưa từng thấy bao giờ, nên mới lên tiếng. |

**Nhận xét khi đối chiếu:** LỖI MẤT Ý: bỏ mục đích “muốn thu thập về tặng cho mẹ”. Không nên chấp nhận output này.

Trạng thái generator: `status=ok`, `fallback=false`.

**Evaluator:** chưa chấm riêng ví dụ này (`evaluation=null`); không có điểm giả.

## Nguồn và cách sử dụng

- Ví dụ 1–3: output CPU đã lưu tại `visp_finetune/reports/local_reload_predictions.jsonl`; evaluator đã chạy thật trên các cặp này.
- Ví dụ 4–6: lấy từ output test hồi cứu tại `visp_finetune/runs/test_predictions.jsonl`; cố ý chọn câu có thay đổi, gồm một lỗi mất ý.
- Generator được train bằng 697 cặp: 476 target giữ nguyên, 221 target thay đổi. Điều này phù hợp với xu hướng ít can thiệp, chưa chứng minh nguyên nhân duy nhất.
- Đây là output generator trước gate; khác với việc gate evaluator chọn giữ câu gốc.
- Giữ `sample_id`, `status`, `fallback`, `error` khi tích hợp. Không coi `status=ok` là bằng chứng chất lượng tốt.
- Rank dùng so phương án cùng source. Điểm không phải xác suất hoặc điểm người đọc 0–100. Timing/sai số số thực có thể khác theo máy.

## JSON đầy đủ trong cùng file

Mở mục dưới để xem/copy dữ liệu cho application. Không cần tải file sample riêng.

<details>
<summary>Xem JSON của cả 6 sample và thông tin nguồn</summary>

```json
{
  "scored_examples_metadata": {
    "description": "Real stored ViSP CPU generation outputs plus actual evaluator CPU scoring; interface examples, not an independent quality benchmark.",
    "generator_output_origin": "visp_finetune/reports/local_reload_predictions.jsonl",
    "source_origin": "visp_finetune/data/inference_example.jsonl",
    "evaluator_scored_at": "2026-11-19T09:47:07.548590+07:00",
    "device": "cpu",
    "generator_sha256": "db9ff2cef0885c53e5e042c437ed4d7adf7b8bce0e0d0a89fd29ac5ac99dbebd",
    "evaluator_encoder_sha256": "1210ff44e553f923f07ef93359dfd542636c6a0217729877287b36289a481473",
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
        "rank_score": 0.03741016238927841,
        "fluency_delta_proxy": 0.06693083047866821,
        "semantic_preservation_proxy": 0.8051238059997559,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.13823243333354185,
        "latency_scope": "model_forward_excludes_tokenization"
      }
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
        "fluency_delta_proxy": 0.06568525731563568,
        "semantic_preservation_proxy": 0.8544645309448242,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.13823243333354185,
        "latency_scope": "model_forward_excludes_tokenization"
      }
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
        "fluency_delta_proxy": 0.061544548720121384,
        "semantic_preservation_proxy": 0.5856443643569946,
        "grammar_score": null,
        "evaluator_version": "7b45b3a236b099d7",
        "context_used": false,
        "human_validated": false,
        "label_origin": "automatic_proxy_and_legacy_inferred_preference",
        "score_contract": "raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration",
        "latency_seconds_per_pair": 0.13823243333354185,
        "latency_scope": "model_forward_excludes_tokenization"
      }
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
      "evaluation": null,
      "evaluation_status": "not_scored_in_this_addendum"
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
      "evaluation": null,
      "evaluation_status": "not_scored_in_this_addendum"
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
      "evaluation": null,
      "evaluation_status": "not_scored_in_this_addendum"
    }
  ]
}
```

</details>
