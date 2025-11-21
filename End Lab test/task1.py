"""
task1.py

Creates a simple prompt-engineered wrapper and a mock AI model to convert
long clinical doctor notes into short structured summaries.

Includes:
- summarize_clinical_note: main function that prepares a prompt and calls the model
- mock_ai_model: a substitute for an actual AI model (keeps this runnable offline)
- Example prompt template used for real AI services
- At least 3 test cases in __main__

This file is intentionally simple and designed for demonstration and testing.
"""
from typing import Callable
import re


def mock_ai_model(prompt: str) -> str:
    """A mock AI model that simulates converting a prompt + note into a summary.

    This implementation is a heuristic/simple rule-based extractor intended for
    offline testing. A production version would call an external LLM API and
    return the model's response.

    Args:
        prompt: The complete prompt text (including instructions and the note).

    Returns:
        A short structured summary as a string.
    """
    # Try to find common clinical sections/keywords in the prompt/note
    # and synthesize a short structured summary.
    # Lowercase copy for searching
    text = prompt.lower()

    def find_first(keywords):
        for kw in keywords:
            idx = text.find(kw)
            if idx != -1:
                # return a short snippet after keyword
                snippet = prompt[idx: idx + 300]
                # keep first sentence-like chunk
                m = re.search(r"([^.\n]+[.\n]?)", snippet)
                return m.group(1).strip() if m else snippet.strip()
        return ""

    cc = find_first(["chief complaint", "cc:", "presenting", "presenting complaint"]) or "Not specified"
    history = find_first(["history of present", "hpi:", "history:", "history of present illness"]) or "Not specified"
    assessment = find_first(["assessment:", "diagnosis", "impression:"]) or "Not specified"
    plan = find_first(["plan:", "recommendations:", "rx:", "prescribe"]) or "Not specified"

    # Try to extract medications and allergies using regex
    meds = re.findall(r"(?:medication[s]?|meds|rx)[:\s]*([^\n]+)", prompt, flags=re.IGNORECASE)
    meds_text = meds[0].strip() if meds else "None documented"

    allergies = re.findall(r"allerg(?:y|ies)[:\s]*([^\n]+)", prompt, flags=re.IGNORECASE)
    allergies_text = allergies[0].strip() if allergies else "None documented"

    summary = (
        f"Chief Complaint: {cc}\n"
        f"History (brief): {history}\n"
        f"Assessment: {assessment}\n"
        f"Plan: {plan}\n"
        f"Medications: {meds_text}\n"
        f"Allergies: {allergies_text}"
    )

    # Keep the summary concise: max ~500 chars
    return summary if len(summary) <= 1000 else summary[:1000] + "..."


PROMPT_TEMPLATE = (
    "You are an assistant that converts long clinical doctor notes into a "
    "short structured summary. Output must be short and use the following fields: "
    "Chief Complaint, History (brief), Assessment, Plan, Medications, Allergies.\n\n"
    "Note:\n"  # the actual note will be appended after this template
)


def summarize_clinical_note(note: str, model: Callable[[str], str] = None) -> str:
    """Generate a short structured summary from a clinical doctor note.

    This function demonstrates prompt engineering by constructing a clear
    instruction prompt and then calling a provided model function. For testing
    without an external AI, a mock model is used by default.

    Args:
        note: Raw doctor note text (string).
        model: Callable that accepts a prompt string and returns a string.
               If None, mock_ai_model is used.

    Returns:
        A short structured summary string containing the required fields.
    """
    if model is None:
        model = mock_ai_model

    # Build the final prompt. In production one might include examples (few-shot)
    # and constraints (length, style). Keep it explicit to encourage structure.
    prompt = PROMPT_TEMPLATE + "\n" + note

    # Call the model (mock or real) to get the summary
    summary = model(prompt)

    # Post-process: normalize whitespace and ensure shortness
    summary = re.sub(r"\s+\n", "\n", summary.strip())
    return summary


if __name__ == "__main__":
    # Test case 1: typical note with sections
    note1 = (
        "Chief Complaint: Chest pain. History of present illness: 54-year-old male "
        "with sudden onset substernal chest pressure radiating to left arm. "
        "Assessment: Possible acute coronary syndrome. Plan: Obtain EKG, cardiac enzymes, give aspirin. "
        "Medications: Aspirin 81 mg daily. Allergies: Penicillin."
    )

    # Test case 2: short informal note
    note2 = (
        "Pt c/o cough x2 weeks. HPI: productive cough, low-grade fevers, no shortness of breath. "
        "Assessment: Likely bronchitis. Plan: supportive care, albuterol PRN. No known drug allergies."
    )

    # Test case 3: free text with different keywords
    note3 = (
        "Presenting complaint: dizziness. Past medical history: HTN, DM. Impression: orthostatic hypotension. "
        "Recommendations: increase fluids, review antihypertensives. Meds: lisinopril, metformin. Allergies: NKDA."
    )

    for i, n in enumerate((note1, note2, note3), start=1):
        print(f"--- Test case {i} summary ---")
        print(summarize_clinical_note(n))
        print()
"""Clinical note summarization helper.

This module provides `summarize_clinical_note`, a function that uses a
prompt-template plus a mock AI model to convert long doctor notes into
short structured summaries. It includes basic heuristics in the mock
model to simulate an LLM's behavior for testing.

Usage:
	from task1 import summarize_clinical_note
	summary = summarize_clinical_note(long_note_text)
"""
from typing import Dict, Optional
import re

# Prompt template used to instruct an AI model. Kept as a constant to
# make prompt engineering explicit and editable.
PROMPT_TEMPLATE = (
	"You are a clinical summarization assistant. Convert the following "
	"doctor note into a concise structured summary with the fields: "
	"Chief Complaint, History of Present Illness (HPI), Assessment, "
	"Plan, Medications, and Follow-up. Keep each field to one or two "
	"short sentences. Omit extraneous info. If a field is not present, "
	"return an empty string for that field. Note: preserve important "
	"diagnoses and medication names.\n\nNote:\n{note}\n\nSummary:"
)


def mock_ai_model(prompt: str) -> str:
	"""A mock AI model that generates a structured summary string.

	This function simulates an LLM by applying simple heuristics:
	- Look for common headings (Assessment, Plan, Medications, HPI, CC).
	- Fallback: extract the first 1-2 sentences and map into fields.

	It's intentionally simple — replace or wrap a real API call in
	production (e.g., OpenAI, Anthropic) and pass the output through
	a parser that enforces the structured format.
	"""
	# Try to capture explicit headings first
	note = prompt.split('\n\nNote:\n', 1)[1] if '\n\nNote:\n' in prompt else prompt

	def find_heading(heading):
		m = re.search(rf"(?:^{heading}:|\n{heading}:)(.*?)(?:\n\n|\n[A-Z][a-z]+:|$)", note, re.S | re.I)
		return m.group(1).strip() if m else ""

	cc = find_heading('Chief Complaint') or find_heading('CC')
	hpi = find_heading('History of Present Illness') or find_heading('HPI')
	assessment = find_heading('Assessment')
	plan = find_heading('Plan')
	meds = find_heading('Medications') or find_heading('Meds')

	# If nothing found, fallback to simple sentence extraction
	if not any([cc, hpi, assessment, plan, meds]):
		# Split into sentences naively
		sents = re.split(r'(?<=[.!?])\s+', note.strip())
		cc = cc or (sents[0] if sents else "")
		hpi = hpi or (sents[1] if len(sents) > 1 else "")
		assessment = assessment or (sents[2] if len(sents) > 2 else "")
		plan = plan or (sents[3] if len(sents) > 3 else "")

	# Build a compact structured text output (simple parser-friendly).
	parts = [
		f"Chief Complaint: {cc}",
		f"HPI: {hpi}",
		f"Assessment: {assessment}",
		f"Plan: {plan}",
		f"Medications: {meds}",
		f"Follow-up: "
	]
	return "\n".join(parts)


def parse_mock_output(text: str) -> Dict[str, str]:
	"""Parse the mock AI output into a structured dict.

	The mock model returns lines like `Field: value`. This parser splits
	those lines into a dict mapping field -> value, trimming whitespace.
	"""
	out = {}
	for line in text.splitlines():
		if ':' in line:
			key, val = line.split(':', 1)
			out[key.strip()] = val.strip()
	return {
		'Chief Complaint': out.get('Chief Complaint', ''),
		'HPI': out.get('HPI', ''),
		'Assessment': out.get('Assessment', ''),
		'Plan': out.get('Plan', ''),
		'Medications': out.get('Medications', ''),
		'Follow-up': out.get('Follow-up', ''),
	}


def summarize_clinical_note(note: str, model: Optional[callable] = None) -> Dict[str, str]:
	"""Summarize a clinical (doctor) note into a short structured summary.

	Parameters
	- note: The raw clinical note text.
	- model: Optional callable that accepts a prompt string and returns
	  a string response (simulates an LLM). If None, `mock_ai_model` is
	  used.

	Returns a dictionary with keys: 'Chief Complaint', 'HPI', 'Assessment',
	'Plan', 'Medications', 'Follow-up'. Each value is a short string.

	The function demonstrates prompt engineering by constructing a clear
	instruction in `PROMPT_TEMPLATE`, then invoking the model and parsing
	the (mock) response.
	"""
	if model is None:
		model = mock_ai_model

	# Build the prompt for the model
	prompt = PROMPT_TEMPLATE.format(note=note)

	# Call the (mock) model
	raw = model(prompt)

	# Parse into structured dict
	summary = parse_mock_output(raw)

	# Post-process: truncate long values to keep summaries short
	for k, v in summary.items():
		if len(v) > 300:
			summary[k] = v[:297].rstrip() + '...'

	return summary


# ------------------
# Test cases
# ------------------
def _run_tests():
	"""Run quick test cases for `summarize_clinical_note`.

	These are simple demonstrations, not a full test harness. They assert
	that the function returns the expected keys and that some fields are
	non-empty for realistic inputs.
	"""
	notes = []

	# 1) Structured SOAP-style note
	notes.append(
		"Chief Complaint: Chest pain.\nHistory of Present Illness: 58-year-old male "
		"with acute onset chest pressure radiating to left arm. Associated with "
		"nausea and diaphoresis.\nAssessment: Suspected acute coronary syndrome.\n"
		"Plan: Obtain ECG, troponins, start MONA, urgent cardiology consult.\n"
		"Medications: Aspirin 325 mg PO, Nitroglycerin SL PRN.\n"
	)

	# 2) Short free-text note
	notes.append(
		"Pt c/o severe headache for 2 days. BP 160/95. Dx: HTN, tension headache. "
		"Plan: start Lisinopril 10mg qd, follow-up in 1 week."
	)

	# 3) Messy, long paragraph note
	notes.append(
		"56F with history of DM2, HTN, and COPD presents today feeling more "
		"short of breath than usual. She says symptoms worsened over the last "
		"three nights; denies fever but had increased sputum production. On exam "
		"lungs with expiratory wheeze. We will give nebulized albuterol and "
		"steroid burst if no improvement; send sputum culture and chest x-ray. "
		"Current meds include Metformin and Albuterol PRN."
	)

	for i, n in enumerate(notes, 1):
		summary = summarize_clinical_note(n)
		print(f"\nTest case {i} summary:")
		for k, v in summary.items():
			print(f"- {k}: {v}")

		# Basic assertions
		assert set(summary.keys()) == {
			'Chief Complaint', 'HPI', 'Assessment', 'Plan', 'Medications', 'Follow-up'
		}
		# At least one field should be non-empty for realistic notes
		assert any(v for v in summary.values()), "All fields empty in summary!"


if __name__ == '__main__':
	_run_tests()

