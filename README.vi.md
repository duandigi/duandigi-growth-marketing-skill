# Duan Growth Skills 0.2.0

**Bộ Agent Skills theo nguyên tắc evidence-first dành cho Growth Strategy, kết nối tài khoản, dữ liệu đa kênh, AI tự đánh giá, thử nghiệm và tối ưu có phê duyệt.**

Chu trình vận hành:

> kết nối → ánh xạ tài sản → kiểm tra dữ liệu → chuẩn hóa → phân tích từng kênh → AI đánh giá tổng thể → thử nghiệm → phê duyệt → xác minh → học hỏi

## Bản 0.2.0 có gì mới?

- Lập kế hoạch đăng nhập và kết nối tài khoản mà không thu mật khẩu nhà cung cấp.
- Ánh xạ GSC, GA4, Ads, Page, Profile, Location, CRM và WordPress vào đúng dự án.
- Kiểm tra token, quyền, độ mới và tình trạng đồng bộ.
- Chuẩn hóa dữ liệu nhưng không trộn lẫn các khái niệm khác nhau.
- Phân tích từ toàn portfolio đến dự án, kênh, campaign, content, query, landing page, lead và doanh thu.
- Phân tích riêng SEO, Paid Media, Social, Local Search và CRM.
- Phát hiện bất thường, đối chiếu attribution, tính health score có giải thích.
- AI tạo evaluation card: phát hiện, bằng chứng, độ tin cậy, dữ liệu thiếu, ảnh hưởng và hành động tiếp theo.
- Hành động rủi ro phải qua approval, preview, giới hạn, log, xác minh và rollback.
- Có mock connector để cộng đồng thử mà không cần tài khoản thật.

## Tổng cộng 30 skill

### Growth và Experimentation

12 skill gốc về growth model, funnel, opportunity, experiment, growth loop, portfolio, retrospective, engineering brief và ethics.

### Integration và Data Intelligence

`account-connection-planner`, `project-asset-mapping`, `permission-scope-review`, `connection-health-monitor`, `marketing-data-quality-audit`, `cross-channel-data-normalization`

### AI Channel Evaluation

`ai-marketing-evaluator`, `channel-performance-audit`, `seo-channel-analysis`, `paid-media-analysis`, `social-channel-analysis`, `local-search-analysis`, `crm-funnel-analysis`, `marketing-anomaly-detection`, `cross-channel-attribution`, `marketing-health-scoring`, `executive-growth-summary`, `action-approval-planner`

## Điều repo không làm

Repo không chứa token, mật khẩu, cookie, private key hoặc OAuth client secret thật. Repo cũng không tự đăng bài, tự chi tiền quảng cáo, tự nhắn tin hàng loạt hay tự xóa dữ liệu.

Để kết nối tài khoản thật cần triển khai riêng:

- web app và user login;
- OAuth/app của từng nhà cung cấp;
- token vault được mã hóa;
- collector và scheduler;
- database raw + normalized;
- dashboard và approval queue;
- execution adapter đã được kiểm thử.

## Chạy demo không cần tài khoản thật

```bash
python scripts/validate_connections.py examples/multi-channel/mock-connection.json
python scripts/mock_connector.py list-assets examples/multi-channel/mock-connection.json
python scripts/mock_connector.py fetch examples/multi-channel/mock-connection.json
python scripts/normalize_marketing_data.py examples/multi-channel/mock-provider-data.json
python scripts/calculate_health_score.py examples/multi-channel/health-score-input.json
python scripts/detect_anomalies.py examples/multi-channel/anomaly-input.json
```

## Kiểm tra repo

```bash
make validate
```

Tài liệu kiến trúc nằm trong thư mục [`docs/`](docs/). Quy trình đánh giá cộng đồng nằm tại [`benchmarks/README.md`](benchmarks/README.md).

## Nguyên tắc an toàn

- mặc định chỉ đọc;
- không đưa credential vào GitHub hoặc prompt;
- ánh xạ rõ từng tài sản vào tổ chức và dự án;
- dữ liệu lỗi thì AI không được kết luận mạnh;
- AI không tự phê duyệt hành động rủi ro;
- hành động phải có phạm vi, hạn dùng, log, kiểm tra và rollback.

## Giấy phép

MIT. API và tên thương hiệu của nhà cung cấp vẫn chịu điều khoản riêng của họ.
