# Evaluation 

## Questions 

### Do these results match what you found in your previous peer review? Why or why not?
- Some of the results match in previous project like SQL injection, command injection, and insecure HTTP connection vulnerabilities.
- Bandit and Super Linter flagged additional issues, including explicit security misconfigurations and missing error handling.

### Do you think they caught all the vulnerabilities present in the code? Why or why not?
- I think the scanners caught major vulnerabilities but missed simple industry standards like  db_config should use environment variables instead, No sanitization/validation or encryption, encoding, 
- Tools are good for detecting some errors and vulnerabilities, while manual code reviews are better for catching other vulnerabilities and best practices. 

### Why is using multiple code scanners better than using one?

- Less scanners may miss some risks or vulnerabilities, so by using multiple tools, the false-negative rate is reduced, and more risks or vulnerabilities are found.