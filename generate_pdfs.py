# -*- coding: utf-8 -*-
"""
Generates five Task Analysis PDFs for the assignment:
"Leveraging AI Tools to Enhance Task Analysis in UX Design"

Domain chosen: Online Food Delivery Mobile Application
(e.g., Uber Eats, DoorDash, Grubhub, Zomato, Swiggy)

Each PDF covers one of five core user tasks and includes:
  1. User Task (for reference)
  2. Competitive Products (for reference), including shortcomings
  3. Human Factors and Environmental Considerations
  4. Identified Pain Points, Challenges, and Tools Used by Users
"""

from fpdf import FPDF
import os

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Task Analysis PDFs")
os.makedirs(OUTDIR, exist_ok=True)

DOMAIN = "Online Food Delivery Mobile Application"

# ---------------------------------------------------------------------------
# Content data for the five user tasks
# ---------------------------------------------------------------------------

TASKS = [
    {
        "file": "1_Search_and_Select_Restaurant_or_Meal.pdf",
        "name": "Search and Select a Restaurant or Meal",
        "task": {
            "Goal": "Find a restaurant or specific meal that matches the user's "
                    "cravings, dietary restrictions, budget, and available time, "
                    "as quickly and confidently as possible.",
            "Primary Actor": "A hungry user (customer) using a food delivery app.",
            "Trigger": "The user feels hungry, is planning a meal, or needs to "
                       "order food for themselves or a group.",
            "Preconditions": "App is installed, user is logged in, and location "
                              "services are enabled.",
            "Basic Flow": [
                "Open the app; the app detects the user's current location.",
                "User browses the home feed/categories or searches by keyword.",
                "User applies filters (cuisine, price, rating, dietary needs, "
                "delivery time).",
                "User reviews the list of restaurants or dishes returned.",
                "User selects a restaurant and opens its menu.",
                "User selects a specific dish to view details.",
            ],
            "Postcondition": "A restaurant and/or meal is selected and ready to "
                              "be added to the cart.",
        },
        "competitors": [
            ("Uber Eats", "Sponsored/ad-placed restaurants are mixed into organic "
                           "results, cluttering relevance and search trust."),
            ("DoorDash", "No reliable 'open now' filter; closed restaurants "
                         "still appear in search results."),
            ("Grubhub", "Keyword search is literal and does not handle typos "
                        "or synonyms (e.g., 'mexican' misses 'taqueria')."),
            ("Zomato", "Rich discovery content (photos/reviews) loads slowly, "
                       "hurting search speed on weaker connections."),
            ("Swiggy", "Combined filters (e.g., 'pure veg' + 'fast delivery') "
                       "reset when the user navigates back to results."),
        ],
        "human_factors": [
            "Cognitive load: decision fatigue from excessive options leads users "
            "to 'satisfice' rather than find the optimal choice.",
            "Physical context: frequent one-handed use while walking or "
            "commuting requires larger, thumb-friendly tap targets.",
            "Environmental: outdoor glare reduces photo/menu readability; "
            "unstable networks (subways, elevators) cause failed searches.",
            "Time pressure: searches often occur during short lunch breaks, "
            "increasing stress when results load slowly.",
            "Sensory bias: hunger increases reliance on appealing photos over "
            "accurate information (ratings, wait times).",
            "Accessibility: screen-reader users need descriptive alt text for "
            "food images and clearly labeled filter controls.",
        ],
        "pain_points": [
            "Overwhelming number of choices with little personalized guidance.",
            "Irrelevant sponsored results mixed into organic search.",
            "Inconsistent or missing 'open now' status.",
            "Slow-loading search results due to heavy imagery.",
            "Filters that do not persist when navigating back.",
        ],
        "challenges": [
            "Balancing personalization and speed without overwhelming the user.",
            "Surfacing trustworthy ratings while filtering out fake reviews.",
            "Reliably filtering for dietary restrictions (vegan, halal, allergens).",
        ],
        "tools_used": [
            "In-app search bar and filter/sort menus.",
            "Saved favorites and reorder lists.",
            "External review sites (Yelp, Google Reviews) cross-referenced "
            "before deciding.",
            "Screenshots shared with others to make a group decision.",
            "Voice assistants for quick, hands-free queries.",
        ],
    },
    {
        "file": "2_Customize_Order_and_Add_to_Cart.pdf",
        "name": "Customize an Order and Add It to Cart",
        "task": {
            "Goal": "Select the exact item options, quantities, add-ons, and "
                    "special instructions so the final order matches personal "
                    "or dietary preferences.",
            "Primary Actor": "A customer ordering for themselves or a group.",
            "Trigger": "The user has selected a restaurant/menu and wants to "
                       "configure specific items before ordering.",
            "Preconditions": "A restaurant menu is open and at least one item "
                              "is being configured.",
            "Basic Flow": [
                "Open an item and select size or variant.",
                "Select modifiers (toppings, spice level, sides).",
                "Add special instructions or allergy notes.",
                "Set the desired quantity.",
                "Add the item to the cart.",
                "Repeat for additional items, then review the full cart.",
            ],
            "Postcondition": "The cart contains correctly customized items "
                              "ready for checkout.",
        },
        "competitors": [
            ("Uber Eats", "Modifier menus nest many sub-options, requiring "
                          "excessive scrolling and taps for a single item."),
            ("Grubhub", "Special instructions are limited to free text with no "
                       "structured allergy flags, risking miscommunication."),
            ("DoorDash", "Selected modifiers can be silently dropped if the "
                        "user backs out before confirming the item."),
            ("Zomato", "Group ordering lacks a per-person item/cost breakdown "
                      "inside the shared cart."),
            ("Swiggy", "Combo/bundle items lock out individual swaps, forcing "
                      "users to cancel and rebuild the entire combo."),
        ],
        "human_factors": [
            "Cognitive: working-memory strain tracking multiple modifiers "
            "across several items, especially for group orders.",
            "Physical: repetitive small taps on toggles/checkboxes fatigue "
            "users during long customization chains.",
            "Environmental: ordering in noisy or distracting settings (office, "
            "family dinner) leads to rushed, error-prone input.",
            "Emotional: anxiety about allergies or dietary needs not being "
            "clearly communicated to kitchen staff.",
            "Social: group ordering requires coordinating with others outside "
            "the app (texting screenshots), adding extra friction.",
        ],
        "pain_points": [
            "Lost modifiers after navigating back in the app.",
            "Unclear price updates as modifiers are selected.",
            "No structured way to flag allergies or dietary restrictions.",
            "Inability to edit a single item within a combo/bundle.",
        ],
        "challenges": [
            "Designing a modifier UI that is flexible yet simple.",
            "Providing real-time price transparency as options change.",
            "Preventing accidental cart resets or dropped selections.",
        ],
        "tools_used": [
            "In-app cart review screen.",
            "Screenshots and text messages to coordinate group orders.",
            "Notes app to record a 'usual order' for repeat use.",
            "Customer support chat to correct mistakes after submission.",
        ],
    },
    {
        "file": "3_Checkout_and_Payment.pdf",
        "name": "Check Out and Make Payment",
        "task": {
            "Goal": "Confirm delivery details, apply promotions, select a "
                    "payment method, and successfully submit the order.",
            "Primary Actor": "A customer with a finalized cart.",
            "Trigger": "The user has reviewed the cart and is ready to pay.",
            "Preconditions": "Cart contains at least one item; delivery address "
                              "is available or must be set.",
            "Basic Flow": [
                "Review the cart contents and total.",
                "Confirm or edit the delivery address.",
                "Select a delivery time (ASAP or scheduled).",
                "Apply a promo code, if any.",
                "Select a tip amount.",
                "Choose a payment method and confirm the order.",
                "Receive an order confirmation.",
            ],
            "Postcondition": "The order is placed and payment is processed "
                              "successfully.",
        },
        "competitors": [
            ("DoorDash", "A high default tip percentage is pre-selected, and "
                         "the $0 tip option is hard to find."),
            ("Uber Eats", "Service and small-print fees are not clearly "
                          "itemized until the final screen, surprising users."),
            ("Grubhub", "Promo codes often fail silently without explaining "
                       "why (expired vs. ineligible restaurant)."),
            ("Zomato", "Saved payment methods sometimes fail to sync with the "
                      "in-app wallet, forcing re-entry of card details."),
            ("Swiggy", "New addresses lack a map-pin confirmation step, "
                      "sometimes resulting in incorrect delivery locations."),
        ],
        "human_factors": [
            "Cognitive: users must quickly process multiple cost components "
            "(item total, fees, tip, tax), risking error or mistrust.",
            "Trust/emotional: hidden fees and default high tips create "
            "frustration and a feeling of being manipulated.",
            "Physical: entering payment or address details one-handed on a "
            "small screen is error-prone.",
            "Environmental: checkout often happens under time pressure "
            "(hunger, short breaks) or with unstable connectivity, risking "
            "duplicate charges on retry.",
            "Security: users are often wary of saving card data due to data "
            "breach concerns.",
        ],
        "pain_points": [
            "Non-transparent fees revealed late in the checkout flow.",
            "Manipulative default tip amounts.",
            "Promo codes that fail without clear explanation.",
            "Incorrect delivery addresses due to lack of map confirmation.",
            "Failed or duplicate payment attempts on poor connections.",
        ],
        "challenges": [
            "Balancing monetization (fees/tips) with pricing transparency.",
            "Robustly handling network failures during payment without "
            "double-charging the user.",
            "Making promo/discount logic clear and explainable.",
        ],
        "tools_used": [
            "Digital wallets (Apple Pay, Google Pay).",
            "Saved debit/credit cards.",
            "Banking apps to verify charges after checkout.",
            "Screenshots of order confirmations for receipts/reimbursement.",
            "Browser-based coupon sites for promo codes.",
        ],
    },
    {
        "file": "4_Track_Real-Time_Order_Delivery.pdf",
        "name": "Track Real-Time Order Delivery",
        "task": {
            "Goal": "Monitor order preparation and delivery progress to plan "
                    "arrival time and ensure the order is received.",
            "Primary Actor": "A customer waiting for their delivery.",
            "Trigger": "The order has been placed and confirmed by the "
                       "restaurant.",
            "Preconditions": "An active order exists with a tracking status.",
            "Basic Flow": [
                "View the order status screen.",
                "See stage updates (preparing, picked up, en route).",
                "View the live map and courier location.",
                "Receive push notifications for status changes.",
                "Contact the courier or support if an issue arises.",
                "Receive the order and mark it complete.",
            ],
            "Postcondition": "The order is delivered and marked complete, or "
                              "an issue is escalated to support.",
        },
        "competitors": [
            ("Uber Eats", "Live map ETA is frequently inaccurate, swinging "
                          "drastically as the courier takes alternate routes."),
            ("DoorDash", "In-app courier contact (chat/call) is sometimes "
                        "unresponsive due to the courier's own connectivity."),
            ("Grubhub", "Status remains stuck on 'preparing' long after the "
                       "food has actually been picked up."),
            ("Zomato", "No proactive notification when a delivery is delayed; "
                      "the user must manually refresh the app."),
            ("Swiggy", "Continuous GPS polling for the live map drains "
                      "battery quickly, frustrating users with low battery."),
        ],
        "human_factors": [
            "Cognitive: uncertain ETAs trigger an anxious 'app-checking loop'.",
            "Physical/environmental: users may change location before "
            "delivery (different room/building), requiring flexible "
            "last-minute updates.",
            "Context of use: tracking happens alongside other tasks (working, "
            "cooking), requiring glanceable, low-attention notifications.",
            "Device constraints: low battery and weak signal are common near "
            "delivery time, so the tracking UI must be power-efficient and "
            "resilient to connectivity gaps.",
            "Emotional: frustration escalates with inaccurate ETAs, "
            "especially when hungry.",
        ],
        "pain_points": [
            "Inaccurate or constantly shifting ETAs.",
            "Unresponsive courier contact options.",
            "Stale status updates that do not reflect reality.",
            "High battery drain from live tracking.",
            "No proactive alerts for delays.",
        ],
        "challenges": [
            "Providing reliable real-time GPS tracking while managing "
            "battery usage.",
            "Generating realistic, dynamically updated ETAs.",
            "Creating a clear escalation path when deliveries run late.",
        ],
        "tools_used": [
            "Push notifications and lock-screen status widgets.",
            "In-app live map view.",
            "In-app chat/call to courier or support.",
            "External maps (Google Maps) to cross-check courier location.",
        ],
    },
    {
        "file": "5_Rate_Order_and_Resolve_Issues.pdf",
        "name": "Rate the Order and Resolve Delivery Issues",
        "task": {
            "Goal": "Provide feedback on the experience and resolve any "
                    "problems (missing items, wrong order, late delivery, "
                    "quality issues) through refunds or credits.",
            "Primary Actor": "A customer after receiving, or failing to "
                              "receive, their order.",
            "Trigger": "The order is marked delivered, or a problem is noticed "
                       "upon opening it.",
            "Preconditions": "An order exists in a delivered or near-delivered "
                              "state.",
            "Basic Flow": [
                "Receive the delivery and inspect the order.",
                "Rate the restaurant and/or courier.",
                "If an issue is found, open the support/help flow.",
                "Select an issue category and submit evidence (e.g., a photo).",
                "Request a refund or credit.",
                "Receive a resolution from support.",
            ],
            "Postcondition": "Feedback is submitted and/or the issue is "
                              "resolved with a refund or credit.",
        },
        "competitors": [
            ("DoorDash", "An automated chatbot loops through generic FAQs "
                         "before allowing escalation to a human agent."),
            ("Uber Eats", "Refund policy is opaque; users are unsure whether "
                          "an automatic credit or a reviewed refund will apply."),
            ("Grubhub", "The rating prompt appears before the user has "
                       "actually opened and inspected the food."),
            ("Zomato", "No structured photo-upload flow for proving damaged "
                      "or missing items, lengthening dispute resolution."),
            ("Swiggy", "Refund credits are locked to the in-app wallet only, "
                      "with no cash/card refund option."),
        ],
        "human_factors": [
            "Emotional: high frustration when food is wrong, late, or "
            "missing, especially when hungry, requiring empathetic, "
            "fast-resolving UI and copy.",
            "Cognitive: users want a minimal number of steps to report an "
            "issue while already frustrated; long forms increase abandonment.",
            "Physical: capturing evidence photos of food/packaging often "
            "happens under poor lighting (home kitchen at night).",
            "Trust: repeated minor issues erode long-term trust in the "
            "platform; users compare complaint-process friction across apps.",
            "Social: users may vent on social media if in-app resolution "
            "feels inadequate, amplifying reputational risk.",
        ],
        "pain_points": [
            "Chatbot loops that delay reaching a human agent.",
            "Unclear refund policy and resolution timeline.",
            "Rating prompts that appear before the order is inspected.",
            "Cumbersome evidence submission (no structured photo upload).",
            "Refunds restricted to in-app wallet credit only.",
        ],
        "challenges": [
            "Balancing fraud prevention with fast, low-friction resolution.",
            "Timing the rating prompt appropriately after delivery.",
            "Offering flexible refund methods (cash/card vs. credit).",
        ],
        "tools_used": [
            "In-app help/support chat.",
            "Phone camera for evidence photos.",
            "Email and order receipts as records.",
            "Social media or public reviews as an escalation tool.",
            "Banking/payment apps to verify refunds.",
        ],
    },
]

# ---------------------------------------------------------------------------
# PDF rendering
# ---------------------------------------------------------------------------

NAVY = (25, 55, 95)
GRAY = (90, 90, 90)
LIGHT = (235, 240, 247)


class TaskPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*GRAY)
        half = (self.w - self.l_margin - self.r_margin) / 2
        self.cell(half, 8, self.title_text, align="L", new_x="RIGHT", new_y="TOP")
        self.cell(half, 8, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*GRAY)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section_title(self, number, text):
        self.ln(3)
        self.set_fill_color(*NAVY)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 9, f"  {number}. {text}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.set_text_color(0, 0, 0)

    def label(self, text):
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(*NAVY)
        self.cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10.5)
        self.multi_cell(0, 5.5, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def bullet_list(self, items):
        self.set_font("Helvetica", "", 10.5)
        left = self.l_margin
        for item in items:
            y = self.get_y()
            self.set_xy(left, y)
            self.cell(5, 5.5, chr(149))  # bullet character (core font safe)
            self.set_xy(left + 5, y)
            self.multi_cell(0, 5.5, item, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def numbered_list(self, items):
        self.set_font("Helvetica", "", 10.5)
        left = self.l_margin
        for i, item in enumerate(items, 1):
            y = self.get_y()
            self.set_xy(left, y)
            self.cell(7, 5.5, f"{i}.")
            self.set_xy(left + 7, y)
            self.multi_cell(0, 5.5, item, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)


def build_pdf(task_info):
    pdf = TaskPDF(format="A4")
    pdf.title_text = f"Task Analysis - {task_info['name']}"
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(18, 15, 18)
    pdf.add_page()

    # --- Cover / title block ---
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(0, 9, "Task Analysis Using AI Tools", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 13)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 8, task_info["name"], align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "I", 10.5)
    pdf.set_text_color(*GRAY)
    pdf.multi_cell(0, 6, f"Domain: {DOMAIN}", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.set_draw_color(*NAVY)
    pdf.set_line_width(0.6)
    pdf.line(18, pdf.get_y(), pdf.w - 18, pdf.get_y())
    pdf.ln(6)
    pdf.set_text_color(0, 0, 0)

    # --- Section 1: User Task for reference ---
    pdf.section_title(1, "User Task (For Reference)")
    t = task_info["task"]
    pdf.label("Goal:")
    pdf.body_text(t["Goal"])
    pdf.label("Primary Actor:")
    pdf.body_text(t["Primary Actor"])
    pdf.label("Trigger:")
    pdf.body_text(t["Trigger"])
    pdf.label("Preconditions:")
    pdf.body_text(t["Preconditions"])
    pdf.label("Basic Flow:")
    pdf.numbered_list(t["Basic Flow"])
    pdf.label("Postcondition:")
    pdf.body_text(t["Postcondition"])

    # --- Section 2: Competitive products ---
    pdf.section_title(2, "Competitive Products for Reference (Shortcomings)")
    with pdf.table(
        col_widths=(32, 68),
        text_align=("LEFT", "LEFT"),
        line_height=5,
        cell_fill_color=LIGHT,
        cell_fill_mode="ROWS",
        borders_layout="ALL",
    ) as table:
        header_row = table.row()
        header_row.cell("Product")
        header_row.cell("Identified Shortcoming")
        for name, shortcoming in task_info["competitors"]:
            row = table.row()
            row.cell(name)
            row.cell(shortcoming)

    # --- Section 3: Human factors and environmental considerations ---
    pdf.section_title(3, "Human Factors and Environmental Considerations")
    pdf.bullet_list(task_info["human_factors"])

    # --- Section 4: Pain points, challenges, tools used ---
    pdf.section_title(4, "Pain Points, Challenges, and Tools Used by Users")
    pdf.label("Pain Points:")
    pdf.bullet_list(task_info["pain_points"])
    pdf.label("Challenges:")
    pdf.bullet_list(task_info["challenges"])
    pdf.label("Tools Used by Users:")
    pdf.bullet_list(task_info["tools_used"])

    out_path = os.path.join(OUTDIR, task_info["file"])
    pdf.output(out_path)
    print(f"Created: {out_path}")


if __name__ == "__main__":
    for task_info in TASKS:
        build_pdf(task_info)
    print(f"\nAll PDFs saved to: {OUTDIR}")
