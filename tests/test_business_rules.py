from business_rules import (
    calculate_print_cost, 
    get_volume_discount, 
    calculate_job_total,
    requires_proof,
    needs_overnight_run,
    total_invoiced,
    largest_job, 
    format_job_line,
)


def test_print_cost_multiples_price_and_copies():
    assert round(calculate_print_cost(0.25, 100), 2) == 25.00

def test_discount_199_copies_has_no_discount():
    assert get_volume_discount(199) == 0.0

def test_discount_200_copies_is_8_percent():
    assert get_volume_discount(200) == 0.08

def test_discount_999_copies_is_8_percent():
    assert get_volume_discount(999) == 0.08

def test_discount_1000_copies_is_15_percent():
    assert get_volume_discount(1000) == 0.15

