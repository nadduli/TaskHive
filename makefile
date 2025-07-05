# Makefile to run SkillBridge app

.PHONY: run

run:
	uvicorn app.main:app --reload
