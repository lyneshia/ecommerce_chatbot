from semantic_router import Route, SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder


# --------------------------------------------------
# 1. Initialize the embedding encoder
# --------------------------------------------------

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-distilroberta-v1"
)


# --------------------------------------------------
# 2. Define FAQ route
# --------------------------------------------------

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy for the products?",
        "What are the payment options for the products?",
        "Is cash on delivery accepted?",
        "Do I get a discount with an HDFC Credit Card?",
        "How can I track my order?",
        "How to track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "Do you accept UPI payments?",
        "How to contact customer support?",
        "What is the policy for defective products?",
        "Can I return a product?",
        "How do I get a refund?",
        "Can I return my product after 60 days?",
        "I want to contact the customer support team",
        "What happens if I receive a damaged product?",
        "Do you accept returns after 30 days?",
        "How can I cancel my order?",
        "How long does it take to deliver the product?",
        "What is the average delivery time?",
        "Can I take the shipment after opening and checking the contents inside?",
        "When will I get my order once its status changes to 'Out for Delivery'?",
        "When do I need to share the OTP with the delivery executive?",
        "How will I get to know if the chosen item is eligible for Open Box delivery?",
        "Is Open Box delivery available for orders placed via Cash on Delivery option?",
        "Why does it take time for the refund amount to be credited when it was already processed by Flipkart?",
        "What is Flipkart's credit card EMI payment option?",
        "Can I use any Debit Card to pay for my order?",
        "Can I change the address for the pick-up the of item(s) in my order?",
        "What i am getting charged for return? Can it be waived off?",
        "What are the checks done for an item that I'm returning?",
        "Can I modify/change the specification for the ordered product without cancelling it?",
        "How long does it take to cancel an order?",
        "Who can use Flipkart EMI?",
        "Why i am getting charged for cancellation? / What is cancellation Fee?",
        "What is the cancellation policy?",
        "I want to cancel my order",
        "Can I return my order?",
        "How much is the cancellation fee?",
        "Can I buy a product through EMI?",
        "What is the EMI policy?",
    ],
)


# --------------------------------------------------
# 3. Define SQL/Product Search route
# --------------------------------------------------

sql = Route(
    name="sql",
    utterances=[
        "I want to buy Nike shoes that have a 50% discount.",
        "What is the price of Puma running shoes?",
        "Are there any Puma shoes on sale?",
        "Do you have formal shoes in size 9?",
        "Are there any shoes under Rs 3000?",
        "Suggest some Nike shoes with a rating of 4 or higher.",
        "Show me Nike shoes under Rs 5000.",
        "Find Puma shoes with a discount.",
        "Which running shoes are available in size 9?",
        "Show me shoes with a rating above 4.",
    ],
)


# --------------------------------------------------
# 4. Create list of routes
# --------------------------------------------------

routes = [faq, sql]


# --------------------------------------------------
# 5. Initialize Semantic Router
# --------------------------------------------------

router = SemanticRouter(
    encoder=encoder,
    routes=routes,
    auto_sync="local",
)
