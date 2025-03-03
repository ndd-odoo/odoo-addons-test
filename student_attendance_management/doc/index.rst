This guide explains how to configure Zalo OA Connector using Zalo for Developer and Zalo OA manager for integration with your system.

Create Zalo Developer Account
=============================

1. **Create an App on Zalo Developer**

   - Follow Zalo guide (switch to English if needed): Visit https://developers.zalo.me/docs/official-account/bat-dau/khoi-tao-ung-dung.

   .. image:: zalo_developer_app.png
      :alt: Creating a Zalo Developer App

2. **Config App on Zalo Developer**

   - In the app dashboard, section **"Sign up to use API"**.
   - Then click **"Official Account API"**.
   - Make sure to enable following API item and click **"Submit for review"**

   .. image:: zalo_api_permissions.png
      :alt: Enabling Zalo API permissions

3. **Configure Official Account Permission Path**

   - Navigate to **Product** > **Official Account** > **General Setting**
   - Fill the **Official Account Callback Url** following format: **https://{your-instance}/zalo/oauth/callback**

   .. image:: zalo_callback_url.png
      :alt: Setting Zalo Callback URL

   - Scoll down and you will see **Select the permissions to request to be granted from OA**, tick all you can then click **Save**

   .. image:: zalo_permissions.png
      :alt: Setting Zalo OA permissions

4. **Retrieve Application ID and Application secret key**

   - Go back to **Setting**
   - You will the **Application ID** and **Application secret key**
   - Copy these value and secure for later on to use on Odoo instance

   .. image:: zalo_app_credentials.png
      :alt: Zalo App Credentials

5. **Configure Webhook**

   - To receive messages or events, configure the **Webhook**:

     - In the **"API and Authorization"** click **"Configure"**.
     - Add your **Webhook URL** following format: **https://{your-instance}/zalo/webhook**.
     - Enable **Webhook Retry**
     - Enable following events (Event Name):
        - user_send_location
        - user_send_image
        - user_send_link
        - user_send_text
        - user_send_sticker
        - user_send_gif
        - user_received_message
        - user_seen_message
        - user_send_audio
        - follow
        - unfollow
        - oa_send_text
        - oa_send_image
        - oa_send_list
        - oa_send_gif
        - user_send_video
        - user_send_file
        - user_reacted_message
        - oa_reacted_message
        - oa_send_sticker
        - user_send_business_card

   .. image:: zalo_webhook_config.png
      :alt: Configuring Zalo Webhook

Helpful Links
=============

- Zalo Developer Overview https://developers.zalo.me/docs/official-account/bat-dau/kham-pha
- Webhook Overview https://developers.zalo.me/docs/official-account/webhook/tong-quan

Create Zalo OA Account
======================

This guide explains how to create Zalo OA, you can skip this part if you already have one or if you want to create a test zalo OA account you can still view this.

1. **Create a Zalo Official Account**

- Follow the instruction at https://oa.zalo.me/home/documents/guides/khoi-tao-zalo-official-account_61 to create new Zalo OA account.
- In case you want to create a test account for testing the integration before using the real account, please visit https://oa.zalo.me/home/documents/guides/tao-tai-khoan-oa-thu-nghiem-ky-thuat_4023591696049457534

   .. image:: zalo_oa_creation.png
      :alt: Creating a Zalo Official Account

Configuring Zalo OA Account in the Software
===========================================

After setting up the Zalo Developer Account and Zalo OA account, configure your Zalo OA account in the software as follows:

Steps to Config Zalo OA Account
===============================

1. **Navigate to Zalo Account Configuration**

   - Go to **Configuration > Zalo Accounts** in the software.
   - Click **"Create"** to add a new Zalo OA account.

   .. image:: zalo_account_list.png
      :alt: Zalo Account List

2. **Enter Required Details**

   - Fill in the following fields:

     - **Name**: Enter a recognizable name for the account e.g., "Main Zalo" (This name will be updated when we connect to zalo).
     - **App ID**: Fill this will Application ID from the Zalo Developer Dashboard in previous step.
     - **App Secret**: Fill this will Application Secret from the Zalo Developer Dashboard in previous step.
     - **Company**: Select the company to associate with this Zalo account.
     - **Notify Users**: Select the users who will receive notifications of incoming messages.

   .. image:: zalo_account_form.png
      :alt: Zalo account configuration form

3. **Connect Zalo OA**

   - Click button **Connect Zalo OA**
   - System will redirect you to a login form where you will select your Zalo OA account to give permission to
   - Click **Allow** in that form and system will redirect back to the original Zalo OA account in odoo if success

   .. image:: zalo_connect_oa.png
      :alt: Connecting to Zalo OA

   .. image:: zalo_account_connected.png
      :alt: Zalo account after connection

Configurate Zalo Message Templates
==================================

Follow these steps to create and manage Zalo message templates.

1. **Navigate to Zalo Templates**

   - Go to **Templates** in the software.
   - Click **"Create"** to add a new template.

   .. image:: zalo_template_list.png
      :alt: Zalo Template List

2. **Fill in Template Details**

   - **Name**: Provide a recognizable name for the template.
   - **Zalo Account**: Select the linked Zalo account.
   - **Template Type**: Select "OA Template" (Official Account Template).
   - **Apply to**: Specify the model you need to apply (e.g., Sale Order, Invoice).
   - **Zalo User Field**: Specify the field containing the recipient's Zalo user ID (default: zalo_user_id).

   .. image:: zalo_template_form.png
      :alt: Zalo Template Configuration Form

3. **Choose Message Type**

   Zalo OA provides three types of messages, each with specific purposes and limitations:

   a. **Consultation Message**

      - Used for direct customer support and inquiries
      - Can be sent within 48 hours after customer interaction
      - No limit on number of messages
      - Configuration:
         - Select **Message Type**: "Consultation Message"
         - Enter message content in **Body Content** field
         - Optionally add media attachments
         - Note: Consultation messages cannot have headers, buttons, or tables

         .. image:: zalo_template_cs.png
            :alt: Zalo Consultation Template

   b. **Transaction Message**

      - Used for order updates, delivery notifications, billing information, etc.
      - No time restriction for sending
      - Requires transaction-related information
      - Configuration:
         - Select **Message Type**: "Transaction Message"
         - Choose appropriate **Transaction Type** (Order, Billing, Reward, etc.)
         - Upload a banner image (required)
         - Add **Header** text (required, max 100 characters)
         - Enter **Body Content**
         - Configure transaction table (see below)
         - Add buttons (optional, max 4)

         .. image:: zalo_template_transaction.png
            :alt: Zalo Transaction Template

   c. **Promotional Message**

      - Used for marketing campaigns, promotions, news, etc.
      - Limited by Zalo's sending quotas
      - Configuration:
         - Select **Message Type**: "Promotional Message"
         - Upload a banner image (required)
         - Add **Header** text (required, max 100 characters)
         - Enter **Body Content**
         - Add buttons (optional, max 4)

         .. image:: zalo_template_promotion.png
            :alt: Zalo Promotional Template

4. **Configure Media Attachments**

   - Select **Attachment Type**: None, Image, Document
   - Upload the corresponding file:
      - Images: JPG or PNG format
      - Documents: PDF format
   - Note: Only one media attachment is allowed per template

   .. image:: zalo_template_media.png
      :alt: Zalo Template Media Configuration

5. **Configure Transaction Tables (for Transaction Messages)**

   Transaction tables display structured information about the transaction:

   - Click **"Add a line"** under the Tables section
   - For each table row:
      - **Label**: Enter a name for the row (max 30 characters)
      - **Field**: Click to open the field selector dialog
         - You can search for fields by name (e.g., search "Currency" to find currency-related fields)
         - For related fields, first select the relation field (e.g., "Currency"), then navigate to its related fields
         - The system will show available fields based on the selected model
         - Select the desired field (e.g., "Symbol")
      - **Sample Value**: Enter a value for preview purposes
   - You can add up to 5 rows in a table

   .. image:: zalo_template_tables.png
      :alt: Zalo Template Tables Configuration

   .. note::
      The field selector makes it easy to find and select fields, even from related models, without having to manually type field paths.

6. **Configure Buttons**

   For Transaction and Promotional messages, you can add interactive buttons:

   - Click **"Add a line"** under the Buttons section
   - For each button:
      - **Title**: Enter button text (max 100 characters)
      - **Type**: Select button type:
         - **Open URL**: Opens a web link
         - **Show Query**: Shows a query message
         - **Hide Query**: Sends a hidden query
         - **Phone Call**: Opens phone dialer
         - **SMS**: Opens SMS composer
      - Based on button type, fill additional fields:
         - For URL buttons: Enter the URL (can include variables like https://example.com/orders/1)
         - For Phone/SMS buttons: Enter phone number
         - For Query buttons: Enter content payload

   .. image:: zalo_template_buttons.png
      :alt: Zalo Template Buttons Configuration

   .. note::
      You can add up to 4 buttons per template

7. **Request User Info (Optional)**

   For templates that need to collect user information:

   - Enable **Request User Info** option
   - Upload an image (required)
   - Add **Header** text (required, max 100 characters)
   - Enter **Body** text (required, max 500 characters)

   .. image:: zalo_template_user_info.png
      :alt: Zalo Template User Info Configuration

8. **Preview Your Template**

   - The system provides a real-time preview of how your template will appear
   - Check all elements (header, body, tables, buttons) for correct formatting

   .. image:: zalo_template_preview.png
      :alt: Zalo Template Preview

Important Notes on Message Types
--------------------------------

1. **Consultation Messages**

   - Can only be sent within 48 hours after customer interaction
   - Cannot have headers, buttons, or tables
   - Best for customer support and direct communication

2. **Transaction Messages**

   - Must be directly related to customer transactions
   - Require a banner image and header
   - Must include transaction details in table format
   - Transaction type must match the actual content

3. **Promotional Messages**

   - Subject to Zalo's sending quotas and policies
   - Require a banner image and header
   - Must comply with Zalo's advertising policies
   - Best for marketing campaigns and announcements

For more detailed information about Zalo message types and requirements, please refer to the official Zalo OA documentation https://developers.zalo.me/docs/official-account/tin-nhan/tong-quan.

Sending Messages with Zalo Templates
=========================================

1. **Navigate to the Record**

   - Go to the record/document (e.g., Sales Order, Invoice, Partner) where you want to send the message.

2. **Access Zalo Composer**

   - Click the **"Zalo"** button in the chatter area of the record.
   - The system will automatically find templates compatible with the current record type.
   - If no template is found, you'll be prompted to configure one.

   .. image:: zalo_chatter_button.png
      :alt: Zalo Button in Chatter

   .. image:: zalo_composer_form.png
      :alt: Zalo Composer Form

3. **Preview and Send**

   - Review the template preview showing how your message will appear to the recipient.
   - The template will automatically populate with data from the current record.
   - Click **"Send"** to dispatch the message via Zalo API.

   .. image:: zalo_message_preview.png
      :alt: Zalo Message Preview

4. **Track Message Status**

   - The Zalo icon next to the message indicates its current status:
      - **Gray**: Queued for sending (queue)
      - **Green**: Successfully sent (sent)
      - **Light Blue**: Delivered to device (delivered)
      - **Teal**: Received by Zalo server (received)
      - **Blue**: Read by recipient (read)
      - **Red**: Sending failed (failed)
   
   - Hover over the icon to see the detailed status message.
   - Status updates automatically as the message progresses through the delivery stages.

   .. image:: zalo_message_status.png
      :alt: Zalo Message Status Indicators

5. **Batch Sending**

   - For multiple records, select them in list view and use the **"Send Zalo Message"** action from the Action menu.
   - This allows efficient communication with multiple customers at once.

   .. image:: zalo_batch_send.png
      :alt: Zalo Batch Sending

Sending/Receiving Messages in Chat Channels
===========================================

When you send a template message to a customer and they reply, the system will use your webhook configuration to automatically create a Zalo chat channel and post messages to it.
The system supports various message types for both sending and receiving, including: text, images, videos (only for receiving), documents, and reactions.

1. **Open a Chat Channel**

   - Go to **"Discuss"**.
   - Open the Zalo channel under the Zalo section to send a message.

   .. image:: zalo_discuss_section.png
      :alt: Zalo Section in Discuss

2. **Compose a Message**

   - Type your message in the chat box.
   - Add media (e.g., images, documents) if needed.
   - Click **"Send"** to deliver the message to the recipient

   .. image:: zalo_chat_compose.png
      :alt: Composing a Zalo Message

4. **Track Message Status**

   - The Zalo icon next to the message indicates its current status:
      - **Gray**: Queued for sending (queue)
      - **Green**: Successfully sent (sent)
      - **Light Blue**: Delivered to device (delivered)
      - **Teal**: Received by Zalo server (received)
      - **Blue**: Read by recipient (read)
      - **Red**: Sending failed (failed)
   
   - Hover over the icon to see the detailed status message.
   - Status updates automatically as the message progresses through the delivery stages.

   .. image:: zalo_chat_status.png
      :alt: Zalo Chat Message Status

5. **Real-time Message Synchronization**

   - The system processes incoming Zalo messages in real-time through the configured webhook.
   - Supported incoming message types include:
      - Text messages
      - Images and photos
      - Videos
      - Documents and files
      - Stickers and GIFs
      - Reactions to messages
      - Location sharing
      - User profile information
   - All incoming messages are automatically displayed in the corresponding Zalo channel.
   - Users selected in the "Notify Users" section of the Zalo account will receive instant notifications when new messages arrive.

   .. image:: zalo_receive_message.png
      :alt: Zalo Incoming Messages
