"""
 Clinical Note Summarization using Prompt Engineering
"""

def generate_summary_prompt(doctor_notes):
    """
    Creates a structured prompt to convert long doctor notes into a
    short, clean summary using prompt engineering.
    """
    prompt = f"""
    You are a medical summary generator.
    Convert the following long doctor notes into a short structured summary.

    Format:
    - Patient Issue:
    - Diagnosis:
    - Treatment Plan:
    - Follow-up Instructions:

    Notes:
    {doctor_notes}

    Return only the summary.
    """
    return prompt


def ai_model_mock(prompt):
    """
    Mock AI model to simulate summarization.
    In a real-world scenario, this would call an actual AI API.
    """
    # For now, we simply return a static summary for demonstration.
    return "Patient Issue: Fever\nDiagnosis: Viral Infection\nTreatment: Paracetamol\nFollow-up: Rest & fluids."


def summarize_doctor_notes(notes):
    """
    Takes raw doctor notes and returns a structured summary.
    Uses a mock AI function.
    """
    prompt = generate_summary_prompt(notes)
    result = ai_model_mock(prompt)
    return result


# ------------------------------
# UNIT TESTS FOR Q1
# ------------------------------

import unittest

class TestClinicalSummary(unittest.TestCase):

    def test_summary_not_empty(self):
        """Test that summary returns some text."""
        result = summarize_doctor_notes("Patient has fever and cough.")
        self.assertTrue(len(result) > 0)

    def test_summary_contains_expected_keywords(self):
        """Test that mock output contains key sections."""
        result = summarize_doctor_notes("Some note...")
        self.assertIn("Patient Issue", result)
        self.assertIn("Diagnosis", result)

    def test_prompt_generation(self):
        """Ensure prompt includes the doctor notes."""
        prompt = generate_summary_prompt("Severe headache.")
        self.assertIn("Severe headache.", prompt)


if __name__ == "__main__":
    unittest.main()
