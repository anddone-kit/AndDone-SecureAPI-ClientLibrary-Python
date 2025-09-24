# AndDone Client Library - Python

This client library integrates with AndDone's secure APIs.

Please see our developer documentation & API Explorer, linked below, for detailed instructions on how to integrate this into your systems.

**Secure API Python Client**

This Python package is an auto-generated client for the AndDone Secure API, built using the [OpenAPI Generator](https://openapi-generator.tech).

- **API version**: 2.3  
- **Package version**: 1.0.0  
- **Generator version**: 7.9.0  
- **Build package**: `org.openapitools.codegen.languages.PythonClientCodegen`
- **Developer Documentation**: [DevDocs](https://docs.anddone.com/)  
- **API Explorer**: [AndDone API Explorer](https://docs.anddone.com/explorer/)

---

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quickstart](#quickstart)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Authorization](#authorization)
- [Support & Versioning](#support--versioning)

---

## Requirements
- **Python 3.7+**  
- Access to **AndDone Merchant Portal** for API keys.

---

## Installation

The recommended method is via `pip`:

```sh
python -m pip install -r requirements.txt
```

Then import the package:

```python
import openapi_client
```

---

## Configuration

1. **Retrieve Developer Credentials:**
   1. Log in to AndDone Merchant Portal Portal:
      - **UAT**: [https://portal.uat.anddone.com](https://portal.uat.anddone.com)  
      - **Production**: [https://portal.anddone.com](https://portal.anddone.com)
   2. Go to **Developer → API Keys** in the left menu.
   3. Copy:
      - `xApiKey` (API Key)
      - `xAppKey` (App Key)

2. **Determine Your Origin:**  
   The `origin` is your public IP address.  
   Find it by searching **"what's my IP"** in Google or visiting [https://www.whatsmyip.org](https://www.whatsmyip.org).
    1. Contact AndDone support to ensure your origin IP is resitered for use with our secure APIs
    2. Email: [integrations@anddone.com](mailto:integrations@anddone.com)

3. **Optional: Create a Configuration File:**  
   Rename `config.example.json` to `config.json` and fill it with your values:

   ```json
   {
     "xApiKey": "YOUR_API_KEY",
     "xAppKey": "YOUR_APP_KEY",
     "xVersion": "2.3",
     "origin": "YOUR_IP_ADDRESS"
   }
   ```

---

## Quickstart

Here’s a minimal working example to call the **Secure Create Payment Intent API**:

```python

from openapi_client.api.secure_payment_intent_api import SecurePaymentIntentApi

x_api_key = 'YOUR_API_KEY'
x_app_key = 'YOUR_APP_KEY'
x_version = '2.3'
origin = 'YOUR_ORIGIN'

post_body =  {
    "saveForFuture": True,
    "amount": 10000,
    "title": "YOUR UNIQUE TITLE",
    "shortDescription": "shortDescription",
    "paymentDescription": "paymentDescription",
    "invoiceNumber": "postman",
    "expiresIn": "300000",
    "intent": {
        "paymentTypes": [
            "CreditCard", 
            "ACH"
        ]
    },
    "enablePremiumFinance": True,
    "splits": None,
    "additionalDetailsPreference": "NoAdditionalDetails"
}

api_instance = SecurePaymentIntentApi()
response = api_instance.secure_paymentintents_post(
    x_api_key, x_app_key, x_version, origin, post_body
)
print(response)

    
```

## Alternate approach (Using optional config.json)

Here is a more involved installation utilizing the openapi Configuration model.

```python
import json
from openapi_client.rest import ApiException
from openapi_client.api.secure_payment_intent_api import SecurePaymentIntentApi
from pprint import pprint

# Defining the host is optional and defaults to https://api.uat.anddone.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uat.anddone.com"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SecureEmbeddedPremiumFinanceApi(api_client)
    # Load credentials from config.json
    with open('config.json') as f:
      config = json.load(f)
   
    pf_policy_update_request_dto = openapi_client.PFPolicyUpdateRequestDTO() # PFPolicyUpdateRequestDTO | Signature Request details (optional)

    try:
        # This API is will update the policy number
        api_response = api_instance.secure_epf_merchants_quotes_policy_put(config['xApiKey'], config['xAppKey'], config['xVersion'], config['origin'], pf_policy_update_request_dto=pf_policy_update_request_dto)
        print("The response of SecureEmbeddedPremiumFinanceApi->secure_epf_merchants_quotes_policy_put:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecureEmbeddedPremiumFinanceApi->secure_epf_merchants_quotes_policy_put: %s\n" % e)
    
```

---

## API Endpoints

All URIs are relative to:

- **UAT**: `https://api.uat.anddone.com`
- **Production**: `https://api.anddone.com`

<details>
  <summary>Click to view all endpoints</summary>

All URIs are relative to *https://api.uat.anddone.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SecureEmbeddedPremiumFinanceApi* | [**secure_epf_merchants_quotes_policy_put**](docs/SecureEmbeddedPremiumFinanceApi.md#secure_epf_merchants_quotes_policy_put) | **PUT** /secure/epf/merchants/quotes/policy | This API is will update the policy number
*SecureEmbeddedPremiumFinanceApi* | [**secure_epf_quotes_booking_put**](docs/SecureEmbeddedPremiumFinanceApi.md#secure_epf_quotes_booking_put) | **PUT** /secure/epf/quotes/booking | This API will update PFA to book a quote.
*SecureEmbeddedPremiumFinanceApi* | [**secure_epf_quotes_captureesign_put**](docs/SecureEmbeddedPremiumFinanceApi.md#secure_epf_quotes_captureesign_put) | **PUT** /secure/epf/quotes/captureesign | This API will eSign the pfa with insured name.
*SecureEmbeddedPremiumFinanceApi* | [**secure_epf_quotes_generate_post**](docs/SecureEmbeddedPremiumFinanceApi.md#secure_epf_quotes_generate_post) | **POST** /secure/epf/quotes/generate | This API is used to Generate Quotes
*SecureEmbeddedPremiumFinanceApi* | [**secure_epf_quotes_intent_post**](docs/SecureEmbeddedPremiumFinanceApi.md#secure_epf_quotes_intent_post) | **POST** /secure/epf/quotes/intent | This API will return quotes created againsts a payment intent.
*SecureEmbeddedPremiumFinanceApi* | [**secure_epf_quotes_post**](docs/SecureEmbeddedPremiumFinanceApi.md#secure_epf_quotes_post) | **POST** /secure/epf/quotes | This API will return quote by QuoteKey.
*SecureEmbeddedPremiumFinanceApi* | [**secure_epf_retrievepfa_post**](docs/SecureEmbeddedPremiumFinanceApi.md#secure_epf_retrievepfa_post) | **POST** /secure/epf/retrievepfa | This API will return PFA for given quoteKey.
*SecureEmbeddedPremiumFinanceEndorsementsApi* | [**secure_epf_endorsements_post**](docs/SecureEmbeddedPremiumFinanceEndorsementsApi.md#secure_epf_endorsements_post) | **POST** /secure/epf/endorsements | This API will do a check of eligibility of account
*SecureEmbeddedPremiumFinanceEndorsementsApi* | [**secure_epf_quote_endorsement_booking_put**](docs/SecureEmbeddedPremiumFinanceEndorsementsApi.md#secure_epf_quote_endorsement_booking_put) | **PUT** /secure/epf/quote/endorsement/booking | This API will update PFA to book a endorsement quote.
*SecureEmbeddedPremiumFinanceEndorsementsApi* | [**secure_epf_quote_endorsement_post**](docs/SecureEmbeddedPremiumFinanceEndorsementsApi.md#secure_epf_quote_endorsement_post) | **POST** /secure/epf/quote/endorsement | This API will do return a quote for an existing policy or new policy for an existing account
*SecureOrumApi* | [**secure_bankaccounts_details_post**](docs/SecureOrumApi.md#secure_bankaccounts_details_post) | **POST** /secure/bankaccounts/details | This API will request for verified bank account.
*SecureOrumApi* | [**secure_bankaccounts_verify_post**](docs/SecureOrumApi.md#secure_bankaccounts_verify_post) | **POST** /secure/bankaccounts/verify | This API will request for account verification.
*SecureOutboundPaymentsApi* | [**vendorapi_secure_outbound_payments_timelines_post**](docs/SecureOutboundPaymentsApi.md#vendorapi_secure_outbound_payments_timelines_post) | **POST** /vendorapi/secure/outboundPayments/timelines | This API gets outbound payment timelines
*SecureOutboundPaymentsApi* | [**vendorapi_secure_outboundpayments_cancel_post**](docs/SecureOutboundPaymentsApi.md#vendorapi_secure_outboundpayments_cancel_post) | **POST** /vendorapi/secure/outboundpayments/cancel | This API cancel outbound payment request
*SecureOutboundPaymentsApi* | [**vendorapi_secure_outboundpayments_detail_post**](docs/SecureOutboundPaymentsApi.md#vendorapi_secure_outboundpayments_detail_post) | **POST** /vendorapi/secure/outboundpayments/detail | This API fetch outbound payment by paymentId
*SecureOutboundPaymentsApi* | [**vendorapi_secure_outboundpayments_post**](docs/SecureOutboundPaymentsApi.md#vendorapi_secure_outboundpayments_post) | **POST** /vendorapi/secure/outboundpayments | This API creates outbound payment request
*SecureOutboundPaymentsApi* | [**vendorapi_secure_outboundpayments_search_post**](docs/SecureOutboundPaymentsApi.md#vendorapi_secure_outboundpayments_search_post) | **POST** /vendorapi/secure/outboundpayments/search | This API gets all outbound payment
*SecurePaymentBatchingApi* | [**secure_batches_details_post**](docs/SecurePaymentBatchingApi.md#secure_batches_details_post) | **POST** /secure/batches/details | This API is used for getting Secure Payment Batch Details
*SecurePaymentBatchingApi* | [**secure_batches_execute_post**](docs/SecurePaymentBatchingApi.md#secure_batches_execute_post) | **POST** /secure/batches/execute | This API execute on-demand batch transaction.
*SecurePaymentBatchingApi* | [**secure_batches_post**](docs/SecurePaymentBatchingApi.md#secure_batches_post) | **POST** /secure/batches | This API is used for getting Secure Payment Batches
*SecurePaymentBatchingApi* | [**secure_batches_timelines_post**](docs/SecurePaymentBatchingApi.md#secure_batches_timelines_post) | **POST** /secure/batches/timelines | This API will returns batch timeline.
*SecurePaymentBatchingApi* | [**secure_batches_transactions_cancel_post**](docs/SecurePaymentBatchingApi.md#secure_batches_transactions_cancel_post) | **POST** /secure/batches/transactions/cancel | This API cancels transactions from an active batch.
*SecurePaymentIntentApi* | [**secure_paymentintents_expirations_post**](docs/SecurePaymentIntentApi.md#secure_paymentintents_expirations_post) | **POST** /secure/paymentintents/expirations | This API expires the payment Intent or link.
*SecurePaymentIntentApi* | [**secure_paymentintents_post**](docs/SecurePaymentIntentApi.md#secure_paymentintents_post) | **POST** /secure/paymentintents | This API is use to create Secure payment Intent.
*SecurePaymentLinksApi* | [**secure_paymentlinks_details_post**](docs/SecurePaymentLinksApi.md#secure_paymentlinks_details_post) | **POST** /secure/paymentlinks/details | This API is used for getting Payment Links by PaymentLink ID
*SecurePaymentLinksApi* | [**secure_paymentlinks_expirations_post**](docs/SecurePaymentLinksApi.md#secure_paymentlinks_expirations_post) | **POST** /secure/paymentlinks/expirations | This API is used for to set expired payment link
*SecurePaymentLinksApi* | [**secure_paymentlinks_id_put**](docs/SecurePaymentLinksApi.md#secure_paymentlinks_id_put) | **PUT** /secure/paymentlinks/{id} | This API is used to update Payment Links
*SecurePaymentLinksApi* | [**secure_paymentlinks_post**](docs/SecurePaymentLinksApi.md#secure_paymentlinks_post) | **POST** /secure/paymentlinks | This API is used to create Payment Links
*SecurePaymentsApi* | [**secure_payments_export_post**](docs/SecurePaymentsApi.md#secure_payments_export_post) | **POST** /secure/payments/export | This API gets Secure payment by search criteria for the merchant.
*SecurePaymentsApi* | [**secure_payments_post**](docs/SecurePaymentsApi.md#secure_payments_post) | **POST** /secure/payments | This API posts new Secure payment request for the merchant.
*SecurePaymentsApi* | [**secure_payments_search_post**](docs/SecurePaymentsApi.md#secure_payments_search_post) | **POST** /secure/payments/search | This API gets Secure payment by search criteria for the merchant.
*SecurePaymentsApi* | [**secure_paymentsdetails_post**](docs/SecurePaymentsApi.md#secure_paymentsdetails_post) | **POST** /secure/paymentsdetails | This API is used for getting details of Payments
*SecurePremiumFinanceLiteApi* | [**secure_epflite_quotes_generate_post**](docs/SecurePremiumFinanceLiteApi.md#secure_epflite_quotes_generate_post) | **POST** /secure/epflite/quotes/generate | This API is used to generate the quote from the provider.
*SecurePremiumFinanceLiteApi* | [**secure_epflite_quotes_link_post**](docs/SecurePremiumFinanceLiteApi.md#secure_epflite_quotes_link_post) | **POST** /secure/epflite/quotes/link | This API will return quotes created againsts a payment link.
*SecurePremiumFinanceLiteApi* | [**secure_epflite_quotes_paymentlinks_post**](docs/SecurePremiumFinanceLiteApi.md#secure_epflite_quotes_paymentlinks_post) | **POST** /secure/epflite/quotes/paymentlinks | This API is used to create Payment Links
*SecureRefundsApi* | [**secure_refunds_eligibility_post**](docs/SecureRefundsApi.md#secure_refunds_eligibility_post) | **POST** /secure/refunds/eligibility | This API return refund eligibility of a transaction.
*SecureRefundsApi* | [**secure_refunds_post**](docs/SecureRefundsApi.md#secure_refunds_post) | **POST** /secure/refunds | This API will refund a transaction which has been settled by the processor.
*SecureReportsApi* | [**secure_reports_downloads_post**](docs/SecureReportsApi.md#secure_reports_downloads_post) | **POST** /secure/reports/downloads | This API will add system report.
*SecureTokenLinksApi* | [**secure_tokenlinks_details_post**](docs/SecureTokenLinksApi.md#secure_tokenlinks_details_post) | **POST** /secure/tokenlinks/details | This API is used for getting Token Links by TokenLink ID
*SecureTokenLinksApi* | [**secure_tokenlinks_expirations_post**](docs/SecureTokenLinksApi.md#secure_tokenlinks_expirations_post) | **POST** /secure/tokenlinks/expirations | This API expires the token link.
*SecureTokenLinksApi* | [**secure_tokenlinks_list_post**](docs/SecureTokenLinksApi.md#secure_tokenlinks_list_post) | **POST** /secure/tokenlinks/list | This API is used for getting all Token Links for Merchant
*SecureTokenLinksApi* | [**secure_tokenlinks_post**](docs/SecureTokenLinksApi.md#secure_tokenlinks_post) | **POST** /secure/tokenlinks | This API is use to create Secure Token Links
*SecureTokenLinksApi* | [**secure_tokenlinks_put**](docs/SecureTokenLinksApi.md#secure_tokenlinks_put) | **PUT** /secure/tokenlinks | This API will update the expireIn and paymentType of Token Link.
*SecureTokenManagementApi* | [**secure_tokens_activations_delete**](docs/SecureTokenManagementApi.md#secure_tokens_activations_delete) | **DELETE** /secure/tokens/activations | This API is used for deactivating merchant token securely
*SecureTokenManagementApi* | [**secure_tokens_details_post**](docs/SecureTokenManagementApi.md#secure_tokens_details_post) | **POST** /secure/tokens/details | This API is used for getting details of Merchant Token by Token link.
*SecureVendorManagementApi* | [**vendorapi_secure_merchants_vendors_delete_post**](docs/SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_delete_post) | **POST** /vendorapi/secure/merchants/vendors/delete | This API deletes vendor into system
*SecureVendorManagementApi* | [**vendorapi_secure_merchants_vendors_details_post**](docs/SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_details_post) | **POST** /vendorapi/secure/merchants/vendors/details | This API gets details of particular vendor
*SecureVendorManagementApi* | [**vendorapi_secure_merchants_vendors_edit_post**](docs/SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_edit_post) | **POST** /vendorapi/secure/merchants/vendors/edit | This API Updates the existing vendor
*SecureVendorManagementApi* | [**vendorapi_secure_merchants_vendors_post**](docs/SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_post) | **POST** /vendorapi/secure/merchants/vendors | This API creates vendor into system
*SecureVendorManagementApi* | [**vendorapi_secure_merchants_vendors_search_post**](docs/SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_search_post) | **POST** /vendorapi/secure/merchants/vendors/search | This API returns list of all the Vendors of Merchant
*SecureVendorManagementApi* | [**vendorapi_secure_merchants_vendors_suspend_post**](docs/SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_suspend_post) | **POST** /vendorapi/secure/merchants/vendors/suspend | This API suspends vendor into system
*SecureVendorManagementApi* | [**vendorapi_secure_merchants_vendors_timeline_post**](docs/SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_timeline_post) | **POST** /vendorapi/secure/merchants/vendors/timeline | This API gets timeline of particular vendor
*SecureVendorManagementApi* | [**vendorapi_secure_merchants_vendors_unsuspend_post**](docs/SecureVendorManagementApi.md#vendorapi_secure_merchants_vendors_unsuspend_post) | **POST** /vendorapi/secure/merchants/vendors/unsuspend | This API unsuspends vendor into system
*SecureVoidsApi* | [**secure_cancellations_post**](docs/SecureVoidsApi.md#secure_cancellations_post) | **POST** /secure/cancellations | This API cancel a transaction.

</details>

---

## Models

<details>
  <summary>Click to view all models</summary>

 - [BankDetailDto](docs/BankDetailDto.md)
 - [CancelPaymentRequestDTO](docs/CancelPaymentRequestDTO.md)
 - [DataDto](docs/DataDto.md)
 - [GetQuoteKeyRequest](docs/GetQuoteKeyRequest.md)
 - [GetQuoteRequest](docs/GetQuoteRequest.md)
 - [HeadingDto](docs/HeadingDto.md)
 - [MerchantTransactionEntityResponse](docs/MerchantTransactionEntityResponse.md)
 - [MerchantTransactionEntityResponseDataInner](docs/MerchantTransactionEntityResponseDataInner.md)
 - [OutboundPaymentTimelineResponseDTOInner](docs/OutboundPaymentTimelineResponseDTOInner.md)
 - [PFCheckEndorsementsRequest](docs/PFCheckEndorsementsRequest.md)
 - [PFCheckEndorsementsResponse](docs/PFCheckEndorsementsResponse.md)
 - [PFCheckEndorsementsResponseItem](docs/PFCheckEndorsementsResponseItem.md)
 - [PFCheckEndorsementsResponseItemPoliciesInner](docs/PFCheckEndorsementsResponseItemPoliciesInner.md)
 - [PFEndorsementRequest](docs/PFEndorsementRequest.md)
 - [PFEndorsementRequestQuote](docs/PFEndorsementRequestQuote.md)
 - [PFEndorsementRequestQuoteAgent](docs/PFEndorsementRequestQuoteAgent.md)
 - [PFEndorsementRequestQuoteAgentAddress](docs/PFEndorsementRequestQuoteAgentAddress.md)
 - [PFEndorsementRequestQuoteCommunication](docs/PFEndorsementRequestQuoteCommunication.md)
 - [PFEndorsementRequestQuoteDetails](docs/PFEndorsementRequestQuoteDetails.md)
 - [PFEndorsementRequestQuoteDetailsRecurringACH](docs/PFEndorsementRequestQuoteDetailsRecurringACH.md)
 - [PFEndorsementRequestQuoteInsured](docs/PFEndorsementRequestQuoteInsured.md)
 - [PFEndorsementRequestQuoteInsuredAddress](docs/PFEndorsementRequestQuoteInsuredAddress.md)
 - [PFEndorsementRequestQuotePoliciesInner](docs/PFEndorsementRequestQuotePoliciesInner.md)
 - [PFEndorsementRequestQuotePoliciesInnerCompany](docs/PFEndorsementRequestQuotePoliciesInnerCompany.md)
 - [PFEndorsementRequestQuotePoliciesInnerGa](docs/PFEndorsementRequestQuotePoliciesInnerGa.md)
 - [PFEndorsementRequestQuotePoliciesInnerPolicyFeeInner](docs/PFEndorsementRequestQuotePoliciesInnerPolicyFeeInner.md)
 - [PFEndorsementRequestQuotePoliciesInnerTotalPayFundingInner](docs/PFEndorsementRequestQuotePoliciesInnerTotalPayFundingInner.md)
 - [PFEndorsementResponse](docs/PFEndorsementResponse.md)
 - [PFEndorsementResponseItem](docs/PFEndorsementResponseItem.md)
 - [PFEndorsementResponseItemPaymentIntent](docs/PFEndorsementResponseItemPaymentIntent.md)
 - [PFEndorsementResponseItemPaymentIntentIntent](docs/PFEndorsementResponseItemPaymentIntentIntent.md)
 - [PFEndorsementResponseItemQuote](docs/PFEndorsementResponseItemQuote.md)
 - [PFEndorsementResponseItemQuoteESignResult](docs/PFEndorsementResponseItemQuoteESignResult.md)
 - [PFGenerateQuoteResponse](docs/PFGenerateQuoteResponse.md)
 - [PFGenerateQuoteResponseItem](docs/PFGenerateQuoteResponseItem.md)
 - [PFGenerateQuoteResponseItemESignResult](docs/PFGenerateQuoteResponseItemESignResult.md)
 - [PFLiteGenerateQuoteResponse](docs/PFLiteGenerateQuoteResponse.md)
 - [PFLiteGenerateQuoteResponseItem](docs/PFLiteGenerateQuoteResponseItem.md)
 - [PFLiteGenerateQuoteResponseItemESignResult](docs/PFLiteGenerateQuoteResponseItemESignResult.md)
 - [PFLiteGetQuoteRequest](docs/PFLiteGetQuoteRequest.md)
 - [PFLitePaymentLinkRequest](docs/PFLitePaymentLinkRequest.md)
 - [PFLitePaymentLinkRequestCallbackParameters](docs/PFLitePaymentLinkRequestCallbackParameters.md)
 - [PFLitePaymentLinkRequestCustomersInner](docs/PFLitePaymentLinkRequestCustomersInner.md)
 - [PFLitePaymentLinkRequestCustomersInnerAddress](docs/PFLitePaymentLinkRequestCustomersInnerAddress.md)
 - [PFLitePaymentLinkRequestReferenceDataListInner](docs/PFLitePaymentLinkRequestReferenceDataListInner.md)
 - [PFLitePaymentLinkRequestSettings](docs/PFLitePaymentLinkRequestSettings.md)
 - [PFLiteQuoteByPaymentLinkResponse](docs/PFLiteQuoteByPaymentLinkResponse.md)
 - [PFLiteQuoteByPaymentLinkResponsePoliciesInner](docs/PFLiteQuoteByPaymentLinkResponsePoliciesInner.md)
 - [PFLiteQuoteByPaymentLinkResponsePoliciesInnerCarrier](docs/PFLiteQuoteByPaymentLinkResponsePoliciesInnerCarrier.md)
 - [PFLiteSecureQuoteRequest](docs/PFLiteSecureQuoteRequest.md)
 - [PFLiteSecureQuoteRequestInsured](docs/PFLiteSecureQuoteRequestInsured.md)
 - [PFLiteSecureQuoteRequestInsuredAddress](docs/PFLiteSecureQuoteRequestInsuredAddress.md)
 - [PFLiteSecureQuoteRequestMerchant](docs/PFLiteSecureQuoteRequestMerchant.md)
 - [PFLiteSecureQuoteRequestPoliciesInner](docs/PFLiteSecureQuoteRequestPoliciesInner.md)
 - [PFLiteSecureQuoteRequestPoliciesInnerCarrier](docs/PFLiteSecureQuoteRequestPoliciesInnerCarrier.md)
 - [PFLiteSecureQuoteRequestProgram](docs/PFLiteSecureQuoteRequestProgram.md)
 - [PFPolicyUpdateRequestDTO](docs/PFPolicyUpdateRequestDTO.md)
 - [PFPolicyUpdateResponse](docs/PFPolicyUpdateResponse.md)
 - [PFQuoteBookingRequest](docs/PFQuoteBookingRequest.md)
 - [PFQuoteEsignRequest](docs/PFQuoteEsignRequest.md)
 - [PFRetrievePFARequest](docs/PFRetrievePFARequest.md)
 - [PFRetrievePFARequestDTO](docs/PFRetrievePFARequestDTO.md)
 - [PFUpdatePFARequestDTO](docs/PFUpdatePFARequestDTO.md)
 - [PFUpdatePFAResponse](docs/PFUpdatePFAResponse.md)
 - [PagePaymentListResponseDTO](docs/PagePaymentListResponseDTO.md)
 - [PagePaymentListResponseDTODataInner](docs/PagePaymentListResponseDTODataInner.md)
 - [PageVendorResponseDTO](docs/PageVendorResponseDTO.md)
 - [PageVendorResponseDTODataInner](docs/PageVendorResponseDTODataInner.md)
 - [PaymentBatchCancellationRequest](docs/PaymentBatchCancellationRequest.md)
 - [PaymentBatchDetailsResponse](docs/PaymentBatchDetailsResponse.md)
 - [PaymentBatchDetailsResponseTransactionDetailsInner](docs/PaymentBatchDetailsResponseTransactionDetailsInner.md)
 - [PaymentBatchEventLogResponse](docs/PaymentBatchEventLogResponse.md)
 - [PaymentBatchResponse](docs/PaymentBatchResponse.md)
 - [PaymentBatchResponseDataInner](docs/PaymentBatchResponseDataInner.md)
 - [PaymentDetailResponseDTO](docs/PaymentDetailResponseDTO.md)
 - [PaymentIntentExpiresResponse](docs/PaymentIntentExpiresResponse.md)
 - [PaymentIntentRequest](docs/PaymentIntentRequest.md)
 - [PaymentIntentRequestCustomersInner](docs/PaymentIntentRequestCustomersInner.md)
 - [PaymentIntentRequestIntent](docs/PaymentIntentRequestIntent.md)
 - [PaymentIntentRequestPfr](docs/PaymentIntentRequestPfr.md)
 - [PaymentIntentRequestReferenceDataListInner](docs/PaymentIntentRequestReferenceDataListInner.md)
 - [PaymentIntentRequestSplitsInner](docs/PaymentIntentRequestSplitsInner.md)
 - [PaymentIntentResponse](docs/PaymentIntentResponse.md)
 - [PaymentIntentResponseCustomersInner](docs/PaymentIntentResponseCustomersInner.md)
 - [PaymentLinkExpiresResponse](docs/PaymentLinkExpiresResponse.md)
 - [PaymentLinkRequest](docs/PaymentLinkRequest.md)
 - [PaymentLinkRequestSettings](docs/PaymentLinkRequestSettings.md)
 - [PaymentLinkRequestSettingsIntent](docs/PaymentLinkRequestSettingsIntent.md)
 - [PaymentLinkResponse](docs/PaymentLinkResponse.md)
 - [PaymentLinkResponseCallbackParameters](docs/PaymentLinkResponseCallbackParameters.md)
 - [PaymentLinkResponseCustomersInner](docs/PaymentLinkResponseCustomersInner.md)
 - [PaymentLinkResponseCustomersInnerAccountsInner](docs/PaymentLinkResponseCustomersInnerAccountsInner.md)
 - [PaymentLinkResponseDisplaySettings](docs/PaymentLinkResponseDisplaySettings.md)
 - [PaymentLinkResponseDisplaySettingsIntent](docs/PaymentLinkResponseDisplaySettingsIntent.md)
 - [PaymentLinkResponseLineItemsInner](docs/PaymentLinkResponseLineItemsInner.md)
 - [PaymentLinkResponsePaymentsInner](docs/PaymentLinkResponsePaymentsInner.md)
 - [PaymentLinkResponseReferenceDataListInner](docs/PaymentLinkResponseReferenceDataListInner.md)
 - [PaymentListResponseDTO](docs/PaymentListResponseDTO.md)
 - [PaymentRequest](docs/PaymentRequest.md)
 - [PaymentRequestDetailDTO](docs/PaymentRequestDetailDTO.md)
 - [PaymentRequestDto](docs/PaymentRequestDto.md)
 - [PaymentRequestDtoData](docs/PaymentRequestDtoData.md)
 - [PaymentRequestDtoDataRemittanceData](docs/PaymentRequestDtoDataRemittanceData.md)
 - [PaymentRequestTenderInfo](docs/PaymentRequestTenderInfo.md)
 - [PaymentResponseDto](docs/PaymentResponseDto.md)
 - [PaymentTimeLineRequestDto](docs/PaymentTimeLineRequestDto.md)
 - [QuoteRequest](docs/QuoteRequest.md)
 - [QuoteRequestAgent](docs/QuoteRequestAgent.md)
 - [QuoteRequestAgentAddress](docs/QuoteRequestAgentAddress.md)
 - [QuoteRequestDetails](docs/QuoteRequestDetails.md)
 - [QuoteRequestInsured](docs/QuoteRequestInsured.md)
 - [QuoteRequestInsuredAddress](docs/QuoteRequestInsuredAddress.md)
 - [QuoteRequestPoliciesInner](docs/QuoteRequestPoliciesInner.md)
 - [QuoteRequestPoliciesInnerCompany](docs/QuoteRequestPoliciesInnerCompany.md)
 - [QuoteRequestPoliciesInnerGa](docs/QuoteRequestPoliciesInnerGa.md)
 - [QuoteRequestPoliciesInnerGaAddress](docs/QuoteRequestPoliciesInnerGaAddress.md)
 - [QuoteResponse](docs/QuoteResponse.md)
 - [RefundEligibility](docs/RefundEligibility.md)
 - [RemittanceDataDto](docs/RemittanceDataDto.md)
 - [ReportDownloadRequest](docs/ReportDownloadRequest.md)
 - [RowDto](docs/RowDto.md)
 - [SecureBatchExecuteRequest](docs/SecureBatchExecuteRequest.md)
 - [SecureCancelledTransactionResponse](docs/SecureCancelledTransactionResponse.md)
 - [SecureEpfQuotesPost200Response](docs/SecureEpfQuotesPost200Response.md)
 - [SecureMerchantTokenShortResponse](docs/SecureMerchantTokenShortResponse.md)
 - [SecurePaymentBatchDetailsRequest](docs/SecurePaymentBatchDetailsRequest.md)
 - [SecurePaymentDetailsRequest](docs/SecurePaymentDetailsRequest.md)
 - [SecurePaymentLinkRequest](docs/SecurePaymentLinkRequest.md)
 - [SecureTokenLinkByIdResponse](docs/SecureTokenLinkByIdResponse.md)
 - [SecureTokenLinkByIdResponseAccountToken](docs/SecureTokenLinkByIdResponseAccountToken.md)
 - [SecureTokenLinkByIdResponseTimeLineInner](docs/SecureTokenLinkByIdResponseTimeLineInner.md)
 - [SecureTokenLinkExpiredResponse](docs/SecureTokenLinkExpiredResponse.md)
 - [SecureTokenLinkRequest](docs/SecureTokenLinkRequest.md)
 - [SecureTokenLinkResponse](docs/SecureTokenLinkResponse.md)
 - [SecureTokenLinkResponseCustomersInner](docs/SecureTokenLinkResponseCustomersInner.md)
 - [SecureTokenLinkResponseIntent](docs/SecureTokenLinkResponseIntent.md)
 - [SecureTokenLinkUpdateRequest](docs/SecureTokenLinkUpdateRequest.md)
 - [SecureTransactionCancelRequest](docs/SecureTransactionCancelRequest.md)
 - [SecureTransactionDetailDTO](docs/SecureTransactionDetailDTO.md)
 - [SecureTransactionDetailDTOTenderInfo](docs/SecureTransactionDetailDTOTenderInfo.md)
 - [SecureTransactionRefundRequest](docs/SecureTransactionRefundRequest.md)
 - [SecureUpdatePaymentLinkRequest](docs/SecureUpdatePaymentLinkRequest.md)
 - [SecureUpdatePaymentLinkRequestSettings](docs/SecureUpdatePaymentLinkRequestSettings.md)
 - [SecureUpdatePaymentLinkRequestSettingsIntent](docs/SecureUpdatePaymentLinkRequestSettingsIntent.md)
 - [SecureVendorRequestDTO](docs/SecureVendorRequestDTO.md)
 - [SecureVendorResponseDTO](docs/SecureVendorResponseDTO.md)
 - [SecureVendorResponseDTORemittanceAddress](docs/SecureVendorResponseDTORemittanceAddress.md)
 - [SecureVendorStatusRequestDTO](docs/SecureVendorStatusRequestDTO.md)
 - [SecureVendorTimelineRequestDTO](docs/SecureVendorTimelineRequestDTO.md)
 - [SecureVendorUpdateRequestDTO](docs/SecureVendorUpdateRequestDTO.md)
 - [SecureVendorUpdateRequestDTORemittanceAddress](docs/SecureVendorUpdateRequestDTORemittanceAddress.md)
 - [TokenLinkResponse](docs/TokenLinkResponse.md)
 - [TokenLinkResponseDataInner](docs/TokenLinkResponseDataInner.md)
 - [TokenLinkSecureRequest](docs/TokenLinkSecureRequest.md)
 - [TokenLinkSecureRequestCustomersInner](docs/TokenLinkSecureRequestCustomersInner.md)
 - [TokenLinkSecureRequestIntent](docs/TokenLinkSecureRequestIntent.md)
 - [TokenRequest](docs/TokenRequest.md)
 - [TransactionDetailResponse](docs/TransactionDetailResponse.md)
 - [TransactionDetailResponseSplitsInner](docs/TransactionDetailResponseSplitsInner.md)
 - [TransactionDetailResponseTenderInfo](docs/TransactionDetailResponseTenderInfo.md)
 - [TransactionPaymentResponse](docs/TransactionPaymentResponse.md)
 - [TransactionPaymentResponseAchTenderInfo](docs/TransactionPaymentResponseAchTenderInfo.md)
 - [TransactionPaymentResponseAchTenderInfoCommissionType](docs/TransactionPaymentResponseAchTenderInfoCommissionType.md)
 - [TransactionPaymentResponseBillingContact](docs/TransactionPaymentResponseBillingContact.md)
 - [TransactionPaymentResponseBillingContactAddress](docs/TransactionPaymentResponseBillingContactAddress.md)
 - [TransactionPaymentResponseBillingContactName](docs/TransactionPaymentResponseBillingContactName.md)
 - [TransactionPaymentResponseCcTenderInfo](docs/TransactionPaymentResponseCcTenderInfo.md)
 - [TransactionPaymentResponseRefundOrigin](docs/TransactionPaymentResponseRefundOrigin.md)
 - [TransactionPaymentResponseRefundTransactions](docs/TransactionPaymentResponseRefundTransactions.md)
 - [TransactionPaymentResponseRefundTransactionsDataInner](docs/TransactionPaymentResponseRefundTransactionsDataInner.md)
 - [TransactionPaymentResponseTransactionEntitySplitResponsesInner](docs/TransactionPaymentResponseTransactionEntitySplitResponsesInner.md)
 - [TransactionPaymentResponseTransactionResult](docs/TransactionPaymentResponseTransactionResult.md)
 - [TransactionRefundEligibilityRequest](docs/TransactionRefundEligibilityRequest.md)
 - [UpdateIntentRequest](docs/UpdateIntentRequest.md)
 - [VendorRequestDTO](docs/VendorRequestDTO.md)
 - [VendorRequestDTOPhysicalAddress](docs/VendorRequestDTOPhysicalAddress.md)
 - [VendorRequestDTORemittanceAddress](docs/VendorRequestDTORemittanceAddress.md)
 - [VendorResponseDTO](docs/VendorResponseDTO.md)
 - [VendorResponseDTORemittanceAddress](docs/VendorResponseDTORemittanceAddress.md)
 - [VendorResponseDTOTemplate](docs/VendorResponseDTOTemplate.md)
 - [VendorResponseDTOVerificationResultsInner](docs/VendorResponseDTOVerificationResultsInner.md)
 - [VendorTimelineResponseListInner](docs/VendorTimelineResponseListInner.md)
 - [VerificationEntityRequest](docs/VerificationEntityRequest.md)
 - [VerifyBankAccountRequest](docs/VerifyBankAccountRequest.md)
 - [VerifyBankAccountRequestBankAccountEntity](docs/VerifyBankAccountRequestBankAccountEntity.md)
 - [VerifyBankAccountResponse](docs/VerifyBankAccountResponse.md)
 - [VerifyBankAccountResponseHttpResponse](docs/VerifyBankAccountResponseHttpResponse.md)

</details>

---

## Authorization

Authentication is handled via API keys in HTTP headers:

| Key          | Location | Description           |
|--------------|----------|-----------------------|
| **x-api-key** | Header   | Your API key          |
| **x-app-key** | Header   | Your App key          |
| **x-version** | Header   | API version (e.g., 2.3) |
| **origin**    | Header   | Your public IP address |

---

## Support & Versioning

- **API Environments:** Use UAT for testing; switch to Production only after validation.
- **Issues:** Report bugs or request features via the [GitHub Issues](https://github.com/anddone-kit/AndDone-SecureAPI-ClientLibrary-DotNet/issues) page.

---
