function (someJsFile) {
	var problemGenerator = {};

	/*
	 * Constructor function
	 */
	problemGenerator.ProblemGeneratorView = function(difficulty) {
		var self = this;

		self.operators = ['+','-','*','/'];
		self.difficulty = difficulty;

		/*
		 * Get a random digit 1-10
		 */
		self.getDigit = function() {
			return (Math.floor((Math.random() * 10) + 1));
		};

		/*
		 * get random operation +, -, *, /
		 */
		self.getOperator = function(numberOfOperations) {
			return self.operators[Math.floor((Math.random() * numberOfOperations) + 1)];
		};

		/*
		 * get the solution from the problem parameters
		 */
		self.evaluateSolution = function(a, b, operator) {
			var solution = null;

			if (operator === '+') {
				solution = a + b;
			}
			if (operator === '-') {
				solution = a - b;
			}
			if (operator === '*') {
				solution = a * b;
			}
			if (operator === '/') {
				solution = a / b;
			}
			return solution;
		};

		/*
		 * Validate the User's attempt
		 */
		self.isAttemptCorrect = function(attempt, solution) {
			if (attempt === solution) {
				return true;
			} else {
				return false;
			}
		};

		/*
		 * get problem array firstDigit, Operator, secondDigit, solution
		 */
		self.setRandomProblem = function(difficulty) {
			var a = null;
			var b = null;
			var operator = null;
			var solution = null;

			a = self.getDigit();
			b = self.getDigit();

			if (difficulty == 1) operator = 1;
			if (difficulty == 2) operator = self.getOperator(2);
			if (difficulty == 3) operator = self.getOperator(4);

			solution = self.evaluateSolution(a, b, operator);

			return [a, operator, b, solution];
		};

		return self;
	};

	return problemGenerator;
}