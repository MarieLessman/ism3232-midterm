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

def test_job_total_at_40_dollars_has_no_setup_fee():
    assert round(calculate_job_total(40.00, 1), 2) == 40.00

def test_job_total_just_below_40_dollars_adds_setup_fee():
    assert round(calculate_job_total(39.99, 1), 2) == 54.99

def test_job_total_changes_when_student_org_is_true():
    regular = calculate_job_total(0.80, 500, student_org=False)
    student = calculate_job_total(0.80, 500, student_org=True)
    assert round(regular, 2) == 368.00
    assert round(student, 2) == 348.00

def test_proof_not_required_at_300_dollars():
    assert requires_proof(300.00) is False

def test_proof_required_just_over_300_dollars():
    assert requires_proof(300.01) is True

def test_overnight_not_needed_at_500_copies():
    assert needs_overnight_run(500, 100.00) is False

def test_overnight_needed_at_501_copies():
    assert needs_overnight_run(501, 100.00) is True

def test_overnight_not_needed_at_400_dollars():
    assert needs_overnight_run(10, 400.00) is False

def test_overnight_needed_just_over_400_dollars():
    assert needs_overnight_run(10, 400.01) is True

 