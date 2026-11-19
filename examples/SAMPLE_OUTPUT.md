# Sample output chung — ViSP và evaluator

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
    "all_six_examples_rescored_with_identity": true,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
        "latency_seconds_per_pair": 0.04793571666656741,
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
    }
  ]
}
```

</details>
