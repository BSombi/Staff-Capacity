# Copyright (c) 2023, IPC and contributors
# For license information, please see license.txt

import frappe
import statistics
from statistics import mean 
from frappe.model.document import Document


class EmployeePsychometrics(Document):
	
	def before_save(self):
		total_gma = self.verbal_reasoning + self.numerical_reasoning + self.logic_and_reasoning + self.mechanical_reasoning + self.space_relations + self.logic_and_reasoning
		# self.general_mental_ability = statistics.mean(self.verbal_reasoning, self.numerical_reasoning, self.logic_and_reasoning, self.mechanical_reasoning, self.space_relations, self.logic_and_reasoning)
		self.general_mental_ability = total_gma/6

		total_clerical_score = self.analysis_skills + self.proof_reading_skills + self.filing_skills + self.math_skills + self.checking_skills
		self.clerical_overal_score = total_clerical_score/5

		total_critical_thinking = self.critical_thinking_1 + self.critical_thinking_2 + self.critical_thinking_3 + self.critical_thinking_4 + self.critical_thinking_5
		self.critical_thinking_score = total_critical_thinking/5

		total_inbasket = self.decisiveness + self.ability_to_prioritise + self.administrative_skills + self.delegation + self.management_of_surbodinates + self.reasoned_judgement
		self.inbasket_score = total_inbasket/6

		total_assessment = self.communication + self.planninng_and_organising + self.leadership + self.decision_making_and_judgemet + self.teamwork
		self.assessment_centres_score = total_assessment/5

		total_personality = self.service_orientation + self.conscientiousness + self.intellect + self.ambition + self.extroversion + self.openness + self.adjustment
		self.personality_score = total_personality/7
