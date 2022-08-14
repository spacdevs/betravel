unsed:
	@autoflake --in-place --remove-unused-variables --remove-all-unused-import --exclude migrations -r .

format: unsed
	@black -l 79 --exclude="migrations" .
