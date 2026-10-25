from business_rules import (
    calculate_job_total, 
    requires_proof,
    needs_overnight_run,
    total_invoiced, 
    largest_job,
    format_job_line,
)

jobs = [
    {"title": "Flyers", "copy_price": 0.25, "copies": 100, "student_org": False},
    {"title": "Menus", "copy_price": 0.50, "copies": 150, "student_org": True},
    {"title": "Posters", "copy_price": 1.20, "copies": 250, "student_org": False},
    {"title": "Programs", "copy_price": 0.80, "copies": 500, "student_org": True},
    {"title": "Catalogs", "copy_price": 0.40, "copies": 2000, "student_org": False},
    {"title": "Banners", "copy_price": 3.00, "copies": 120, "student_org": False},
    {"title": "Tickets", "copy_price": 0.10, "copies": 501, "student_org": False},
    {"title": "Booklets", "copy_price": 1.75, "copies": 300, "student_org": True},
]

print("Brightline Print Shop - Job Report")

job_count = 0
proof_count = 0
overnight_count = 0

for job in jobs:
    total = calculate_job_total(job["copy_price"], job["copies"], job["student_org"])
    proof = requires_proof(total)
    overnight = needs_overnight_run(job["copies"], total)
    print(format_job_line(job["title"], total, proof, overnight))

job_count = job_count + 1
if proof:
    proof_count = proof_count + 1
if overnight:
    overnight_count = overnight_count + 1

invoiced = total_invoiced(jobs)
average = invoiced / job_count

print(f"Jobs: {job_count}")
print(f"Total invoiced: ${invoiced:.2f}")
print(f"Average job total: ${average:.2f}")
print(f"Largest job total: {largest_job(jobs)}")
print(f"Proofs required: {proof_count}")
print(f"Overnight runs: {overnight_count}")

