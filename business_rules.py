## Business Rules for Brightline Print Shop

# Rule 2: volume discount tiers 
MID_TIER_MIN_COPIES = 200
TOP_TIER_MIN_COPIES = 1000
MID_TIER_DISCOUNT = 0.08
TOP_TIER_DISCOUNT = 0.15
NO_DISCOUNT = 0.0

# Rule 3: student org bonus 
STUDENT_ORG_BONUS = 0.05
STUDENT_ORG_MIN_COPIES = 200

# Rule 4: setup fee
SETUP_FEE = 15.00
SETUP_FEE_THRESHOLD = 40.00

# Rule 5: proof
PROOF_THRESHOLD = 300.00

# Rule 6: overnight run
OVERNIGHT_COPIES_THRESHOLD = 500
OVERNIGHT_TOTAL_THRESHOLD = 400.00

def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Return the print cost before any discount."""
    return copy_price * copies

def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Return the discount rate as a decimal, including the student org bonus."""
    if copies >= TOP_TIER_MIN_COPIES:
        discount = TOP_TIER_DISCOUNT
    elif copies >= MID_TIER_MIN_COPIES:
        discount = MID_TIER_DISCOUNT
    else:
        discount = NO_DISCOUNT

    if student_org and copies >= STUDENT_ORG_MIN_COPIES:
        discount = discount + STUDENT_ORG_BONUS

    return discount 

def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
    """Return the job total: discounted cost plus setup fee when it applies."""
    cost = calculate_print_cost(copy_price, copies)
    discount = get_volume_discount(copies, student_org)
    discounted_cost = cost * (1 - discount)

    if discounted_cost < SETUP_FEE_THRESHOLD:
        discounted_cost = discounted_cost + SETUP_FEE

    return discounted_cost

def requires_proof(total: float) -> bool:
    """Return True when the job total is over the proof threshold."""
    return total > PROOF_THRESHOLD

def needs_overnight_run(copies: int, total: float) -> bool:
    """Return True when copies or the job total exceed the overnight limits."""
    return copies > OVERNIGHT_COPIES_THRESHOLD or total > OVERNIGHT_TOTAL_THRESHOLD

def total_invoiced(jobs: list) -> float:
    """Return the sum of the job totals for every job in the list."""
    running_total = 0.0
    for job in jobs:
        running_total = running_total + calculate_job_total(
           job["copy_price"], job["copies"], job["student_org"] 
        )
    return running_total

def largest_job(jobs: list) -> str:
    """Return the title of the job with the largest total, or "" if empty."""
    best_title = ""
    best_total = None
    for job in jobs:
        total = calculate_job_total(
            job["copy_price"], job["copies"], job["student_org"]
        )
        if best_total is None or total > best_total:
            best_total = total
            best_title = job["title"]
    return best_title

def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:
    """Return one report line with yes/no values and a two-decimal amount."""
    proof_text = "yes" if proof else "no"
    overnight_text = "yes" if overnight_run else "no"
    return f"{title}: ${total:.2f} | proof: {proof_text} | overnight run: {overnight_text}"
