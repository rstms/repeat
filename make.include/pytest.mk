# pytest - testing

options?=-x
testfiles?=$(wildcard tests/test_*.py)
options:=$(if $(test),$(options) -k $(test),$(options))

# pytest   example: make options=-svvvx test=cli test 
test:
	pytest $(options) $(testfiles)

# run pytest, breaking into pdb on exceptions or breakpoints
debug:
	${MAKE} options="$(options) -xvvvs --pdb" test

# show available test cases 
testls:
	@echo $$($(foreach test,$(testfiles),grep '^def test_' $(test);)) |\
	  tr ' ' '\n' | grep -v def | awk -F\( 'BEGIN{xi=0} {printf("%s",$$1);\
	  if(++xi==3){xi=0; printf("\n");} else {printf("\t");}}' |\
	  awk 'BEGIN{print ".TS\nbox,nowarn;\nl | l | l ." } {print} END{print ".TE";}' |\
	  tbl | groff  -T utf8 | awk 'NF';
