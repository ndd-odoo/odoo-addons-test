=============================================
Hướng Dẫn Sử Dụng: Thanh toán QR Tự động BIDV
=============================================

Hướng dẫn này giải thích cách cấu hình và sử dụng mô-đun **Thanh toán QR Tự động BIDV** để thực hiện các giao dịch thanh toán qua mã QR một cách liền mạch.

.. note::
   Hướng dẫn này giả sử bạn đã liên hệ với BIDV, hoàn tất các thỏa thuận cần thiết và nhận được thông tin cấu hình phục vụ cho việc tích hợp.

Cài Đặt
========

#. Truy cập **Ứng dụng (Apps)**.
#. Tìm kiếm với từ khóa *payment_bidv_viin*.
#. Nhấn **Cài đặt (Install)**.

.. image:: doc_install_payment_bidv_viin_vi_VN.png
   :alt: Thanh toán QR Tự động BIDV

Cách Sử Dụng Thanh toán QR Tự động BIDV
=======================================

Cấu Hình Mã đầu Tài khoản định danh
-----------------------------------

1. Đi tới **Cài đặt/Thiết lập**.
2. Trong phần **Thiết lập BIDV**, điền các thông tin sau:

   - **Mã đầu TK định danh:** Do BIDV cung cấp.
   - **Mã dịch vụ:** Mã dịch vụ BIDV cấp cho dịch vụ paygate.
   - **Mã bí mật:** Tự tạo bởi doanh nghiệp và gửi cho BIDV để đảm bảo bảo mật giao dịch.

.. image:: doc_merchant_setting_vi_VN.png
   :alt: Cấu hình Mã đầu TK định danh và Mã bí mật

Bật Tính Năng Thanh Toán QR
----------------------------

1. Đi tới **Cài đặt/Thiết lập**.
2. Trong thanh tìm kiếm, nhập từ khóa **QR** để tìm nhanh.
3. Bật tùy chọn **Mã QR**.

.. image:: doc_qr_enable_vi_VN.png
   :alt: Bật thanh toán QR trong cài đặt

Cấu Hình Tài Khoản Ngân Hàng
----------------------------

1. Vào **Danh bạ** > **Tài khoản Ngân hàng**.
2. Tạo mới hoặc chỉnh sửa tài khoản ngân hàng với các thông tin sau:

   - **Ngân hàng:** Chọn **BIDV** (hãy nhớ điền mã bin chính xác cho BIDV là 970418).
   - **Số tài khoản:** Nhập số tài khoản BIDV.
   - **Chủ tài khoản:** Chọn công ty hiện hành.

.. image:: doc_bank_config_vi_VN.png
   :alt: Cấu hình tài khoản ngân hàng BIDV

3. Trong phần **Cấu hình QR EMV:**

   - **Loại Proxy:** Chọn **Số TK ngân hàng**.
   - **Giá trị Proxy:** Điền số tài khoản ngân hàng (giống như ở trên).

.. image:: doc_emv_config_vi_VN.png
   :alt: Cấu hình QR EMV

4. Trong trường **Kết nối ngân hàng:**  
   - Chọn **BIDV**.  
   - Hệ thống sẽ tự động sinh các thông số cần thiết.  
   - Lưu ý **Khóa đối xứng**, thông tin này cần chia sẻ với BIDV và sử dụng để giải mã dữ liệu.

.. image:: doc_bank_connector_config_vi_VN.png
   :alt: Cấu hình mã đối xứng

Kích Hoạt Nhà Cung Cấp Thanh Toán
---------------------------------

1. Truy cập **Hóa đơn** > **Cấu hình** > **Nhà cung cấp thanh toán**.
2. Tìm **BIDV**
3. Đảm báo trạng thái được là **Đã kích hoạt** and **Đã hiển thị**.

.. image:: doc_enable_bidv_vi_VN.png
   :alt: Kích hoạt thanh toán QR BIDV

Và thế là xong Thanh toán QR Tự động BIDV đã sẵn sàng sử dụng.

.. image:: payment_bidv_overview.jpg
   :alt: Thanh toán QR Tự động BIDV
