# Duandigi Growth Marketing Skills

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-5B5BD6)](https://agentskills.io/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-111111)](https://code.claude.com/docs/en/skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version 0.2.0](https://img.shields.io/badge/version-0.2.0-blue.svg)](CHANGELOG.md)

> **Bộ Agent Skills theo nguyên tắc evidence-first cho growth marketing.** Gồm **30 skill** giúp AI agent chạy trọn một chu trình phân tích **marketing đa kênh** — SEO, Paid Media, Social, Local Search và CRM — cùng kết nối tài khoản an toàn, AI tự đánh giá, thử nghiệm và tối ưu có phê duyệt. Chạy trong **Claude Code** và mọi client tương thích Agent Skills.

Dành cho growth marketer, chuyên viên SEO, người chạy performance, agency và founder SaaS muốn một AI agent suy luận dựa trên **bằng chứng, độ tin cậy và nguồn gốc dữ liệu** — không phán bừa.

[Read in English »](README.md)

---

## Bộ 30 skill làm được gì

Chu trình vận hành:

> **kết nối → ánh xạ tài sản → kiểm tra dữ liệu → chuẩn hóa → phân tích từng kênh → AI đánh giá tổng thể → thử nghiệm → phê duyệt → xác minh → học hỏi**

Mọi kết luận đều gắn với **bằng chứng, độ tin cậy và ghi chú dữ liệu còn thiếu**. Dữ liệu các kênh được giữ nguyên nguồn gốc thay vì trộn lẫn thành con số ảo. Và **mọi hành động rủi ro cao đều phải có người thật phê duyệt** — không tự chi tiền, đăng bài, nhắn tin hay xóa dữ liệu.

## Bản 0.2.0 có gì

- Lập kế hoạch kết nối tài khoản mà không thu mật khẩu nhà cung cấp.
- Ánh xạ GSC, GA4, Google Ads, Meta, WordPress, CRM và webhook vào đúng dự án.
- Kiểm tra token, quyền, độ mới và tình trạng đồng bộ.
- Chuẩn hóa dữ liệu nhưng không trộn lẫn các khái niệm khác nhau.
- Phân tích riêng SEO, Paid Media, Social, Local Search và CRM.
- Phát hiện bất thường, đối chiếu attribution, tính health score có giải thích.
- AI tạo evaluation card: phát hiện, bằng chứng, độ tin cậy, dữ liệu thiếu, ảnh hưởng và hành động tiếp theo.
- Hành động rủi ro phải qua approval, preview, giới hạn, log, xác minh và rollback.
- Có mock connector để thử mà không cần tài khoản thật.

## Dành cho ai

- **Growth marketer & growth engineer** — dựng pipeline thử nghiệm và growth loop dựa trên bằng chứng.
- **Chuyên viên SEO & content** — audit organic, tìm khoảng trống chất lượng, nối Search Console + GA4 với kết quả kinh doanh.
- **Người chạy Paid Media** — phân tích chi tiêu Google Ads, Meta, đối chiếu attribution, bắt bất thường sớm.
- **Agency & consultant** — một lớp phân tích đa kênh, đa khách hàng, cô lập chặt theo dự án.
- **Founder SaaS & indie hacker** — có báo cáo growth và health score mà không cần cả team analytics.

## 30 skill

### Growth và Experimentation

`growth-model-design`, `growth-funnel-analysis`, `growth-opportunity-finder`, `growth-experiment-design`, `growth-experiment-prioritization`, `growth-experiment-analysis`, `growth-loop-design`, `growth-metrics-diagnosis`, `growth-portfolio-management`, `growth-retrospective`, `growth-engineering-brief`, `growth-ethics-review`

### Integration và Data Intelligence

`account-connection-planner`, `project-asset-mapping`, `permission-scope-review`, `connection-health-monitor`, `marketing-data-quality-audit`, `cross-channel-data-normalization`

### AI Channel Evaluation

`ai-marketing-evaluator`, `channel-performance-audit`, `seo-channel-analysis`, `paid-media-analysis`, `social-channel-analysis`, `local-search-analysis`, `crm-funnel-analysis`, `marketing-anomaly-detection`, `cross-channel-attribution`, `marketing-health-scoring`, `executive-growth-summary`, `action-approval-planner`

Kèm **9 Claude Code agent tùy chọn** điều phối integration, data quality, phân tích kênh, đánh giá đa kênh và kiểm soát phê duyệt.

## Cài trong Claude Code

```text
/plugin marketplace add duandigi/duandigi-growth-marketing-skill
/plugin install duandigi-growth-marketing-skill@duan-growth
```

Chạy demo không cần tài khoản thật:

```bash
python scripts/validate_connections.py examples/multi-channel/mock-connection.json
python scripts/mock_connector.py fetch examples/multi-channel/mock-connection.json
python scripts/normalize_marketing_data.py examples/multi-channel/mock-provider-data.json
python scripts/calculate_health_score.py examples/multi-channel/health-score-input.json
```

Kiểm tra repo: `make validate`. Tài liệu kiến trúc trong [`docs/`](docs/), quy trình đánh giá cộng đồng tại [`benchmarks/README.md`](benchmarks/README.md).

## Nguyên tắc an toàn

- mặc định chỉ đọc;
- không đưa credential vào GitHub hoặc prompt;
- ánh xạ rõ từng tài sản vào tổ chức và dự án;
- dữ liệu lỗi thì AI không được kết luận mạnh;
- AI không tự phê duyệt hành động rủi ro;
- hành động phải có phạm vi, hạn dùng, log, kiểm tra và rollback.

Repo **không chứa** token, mật khẩu, cookie, private key hay OAuth client secret thật. Để kết nối tài khoản thật cần triển khai riêng một web app với OAuth, token vault mã hóa, collector, scheduler và execution adapter đã kiểm thử.

## Về tác giả — Duan Digi

**Duandigi Growth Marketing Skills** được tạo và duy trì bởi **Duan Digi** (Hoàng Văn Duẩn) — một growth marketer với **hơn 10 năm digital marketing và SEO**.

Duẩn hiện là **Marketing Manager** (SEO là chuyên môn lõi), có kinh nghiệm vận hành thực chiến qua **e-commerce, print-on-demand (POD) và niche affiliate site** từ 2014. Thế mạnh: **growth SEO, inbound và content strategy, hệ thống performance marketing cho doanh nghiệp SME** — tư duy business-first, làm thật chứ không lý thuyết.

Anh chia sẻ playbook growth và SEO thực chiến tại **[duandigi.com](https://duandigi.com)**.

- 🌐 Website: [duandigi.com](https://duandigi.com)
- 💼 LinkedIn: [linkedin.com/in/duandigi](https://linkedin.com/in/duandigi)
- 🐦 X (Twitter): [x.com/duandigiseo](https://x.com/duandigiseo)
- 📘 Facebook: [facebook.com/duandizi](https://facebook.com/duandizi)
- ✍️ Medium: [medium.com/@duandigi](https://medium.com/@duandigi)
- 🐙 GitHub: [github.com/duandigi](https://github.com/duandigi)

Nếu dự án hữu ích, một ⭐ cho repo sẽ giúp nhiều người khác tìm thấy nó.

## Giấy phép

MIT — xem [`LICENSE`](LICENSE). API và tên thương hiệu của nhà cung cấp vẫn theo điều khoản riêng của họ.
