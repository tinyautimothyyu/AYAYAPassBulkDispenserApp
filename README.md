<div align="center">
  <h3 align="center">AYAYA Pass Bulk Dispenser App</h3>

  <p align="center">
    <strong>A Python app that uses WhatsApp Business API to send a PDF file to each contact in a CSV file.</strong>
  </p>
  <p align="center">
    Timothy Yu | tinyau.yu@outlook.com
  </p>
</div>

## Motivation

As the Richmond Chinese Alliance Church AYAYA congregation has decided to implement the new digital attendance-taking system, all members of the church who are also regular attendees will be given an AYAYA pass. AYAYA welcome team members will scan the barcode on each attendee's pass to record their attendance. To avoid repetition, the digital team aims to find a solution that can send out the passes to all members at once. This repository is used for the R&D of the dispenser app and the instructions to set up access to the WhatsApp Business API.

## Procedures to set up the WhatsApp business API access

### 1. Set up a WhatsApp business account with landline number
1.1 Install the WhatsApp business app on the phone of PIC<br>
1.2 Submit your WhatsApp Business landline number with your country code. Omit the 0 in the code when you enter the number.<br>
1.3 Choose the Call me option to receive the six-digits OTP for verification.<br>
1.4 Answer the call and enter the OTP to be verified.<br>

WhatsApp has stringent policies on bulk messaging to prevent spam. Using a personal account to send mass messages can lead to account suspension if it's detected as spam. A WhatsApp Business account ensures that you are following their commercial messaging policies.

### 2. Set up a Meta Developer account to gain access to WhatsApp business APIs
2.1 Register a Meta develop account with a Faccebook account <a href="https://developers.facebook.com/apps">here</a>.<br>
2.2 Create a WhatsApp app using the "Create app" button on the home page<br>
![Meta Developer Home Page](/screenshots/meta_developer_home.png)
2.3 Once you have created the app, click on the app and it will redirect you to the "App Dashboard".<br>
2.4 Under "Product" section of the vertical side-nav-bar, click on the "WhatsApp" drop-down menu and select "API Setup".<br>
![Meta Developer App Dashboard](/screenshots/meta_app_dashboard.png)
2.5 Mark down the "Temporary access token" which you will need to use to send messages with the dispenser app.<br>
![Access Token](/screenshots/meta_app_access_token.png)
2.6 Note that you will also need the "Phone number ID" to use the dispenser app. By default, the page displays the test number ID. You will need to add the WhatsApp business account to your meta developer account first to obtain your Phone number ID. We will talk about the process below.<br>

### 3. Connect WhatsApp business account to Meta Developer account
3.1 Go to the "Business settings" of your Meta account <a href="https://business.facebook.com/settings/whatsapp-business-accounts/105108609339228?business_id=862046257503790">here</a>.<br>
![Add WhatsApp account](/screenshots/meta_add_account.png)
3.2 Click on "Add" button to add your WhatsApp business landline number.<br>
3.3 Once this process is completed, return to the App Dashboard and select your newly added WhatsApp account.<br>
3.4 Obtain the Phone number ID of your WhatsApp account.<br>

