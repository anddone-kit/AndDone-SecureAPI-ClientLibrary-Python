from openapi_client.api.secure_embedded_premium_finance_api import SecureEmbeddedPremiumFinanceApi
from openapi_client.api.secure_embedded_premium_finance_endorsements_api import SecureEmbeddedPremiumFinanceEndorsementsApi
from openapi_client.api.secure_orum_api import SecureOrumApi
from openapi_client.api.secure_outbound_payments_api import SecureOutboundPaymentsApi
from openapi_client.api.secure_payment_batching_api import SecurePaymentBatchingApi
from openapi_client.api.secure_payment_intent_api import SecurePaymentIntentApi
from openapi_client.api.secure_payment_links_api import SecurePaymentLinksApi
from openapi_client.api.secure_payments_api import SecurePaymentsApi
from openapi_client.api.secure_premium_finance_lite_api import SecurePremiumFinanceLiteApi
from openapi_client.api.secure_refunds_api import SecureRefundsApi
from openapi_client.api.secure_reports_api import SecureReportsApi
from openapi_client.api.secure_token_links_api import SecureTokenLinksApi
from openapi_client.api.secure_token_management_api import SecureTokenManagementApi
from openapi_client.api.secure_vendor_management_api import SecureVendorManagementApi
from openapi_client.api.secure_voids_api import SecureVoidsApi
from openapi_client import Configuration, ApiClient
import json

with open('C:/Work/AndDone_SDKs/anddone-python-sdk-openapi-codegen/config.json') as f:
  config = json.load(f)
x_api_key = config['xApiKey']
x_app_key = config['xAppKey']
x_version = config['xVersion']
origin = config['origin']
# configuration = Configuration(
#     host="https://api2.uat.anddone.com", server_index=1
# )

post_body = {
  "type": "OpenPayment",
  "id": "c5ffedc0-d42e-439e-9efa-526528937e98"
}

api_instance = SecurePaymentsApi()
response = api_instance.secure_paymentsdetails_post(
    x_api_key, x_app_key, x_version, origin, post_body
)
print(response)

# post_body = {
#   "id": "b9a85673-9c47-4554-ac09-b0a2d66cb69a"
# }
#
# api_instance = SecureOrumApi()
# response = api_instance.secure_bankaccounts_details_post(
#     x_api_key, x_app_key, x_version, origin, post_body["id"], 'checking', post_body
# )
# print(response)