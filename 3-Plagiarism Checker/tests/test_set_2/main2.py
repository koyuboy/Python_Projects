#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <stack>
#include <map>

using namespace std;

//Function to return precedence of operators 
int prec(char c)
{
	if (c == '^')
		return 3;
	else if (c == '*' || c == '/')
		return 2;
	else if (c == '+' || c == '-')
		return 1;
	else
		return -1;
}
string infixToPostfix(string s)
{
	stack<char> st;
	st.push('N');
	int l = s.length();
	string ns;
	for (int i = 0; i < l; i++)
	{
		if ((s[i] >= 'a' && s[i] <= 'z') ||
			(s[i] >= 'A' && s[i] <= 'Z'))
			ns += s[i];

		else if (s[i] == '(')

			st.push('(');

		else if (s[i] == ')')
		{
			while (st.top() != 'N' && st.top() != '(')
			{
				char c = st.top();
				st.pop();
				ns += c;
			}
			if (st.top() == '(')
			{
				char c = st.top();
				st.pop();
			}
		}

		else {
			while (st.top() != 'N' && prec(s[i]) <=
				prec(st.top()))
			{
				char c = st.top();
				st.pop();
				ns += c;
			}
			st.push(s[i]);
		}
	}
	while (st.top() != 'N')
	{
		char c = st.top();
		st.pop();
		ns += c;
	}
	return ns;
}
void cleanWhiteSpaces(string& str)
{
	for (int i = 0; i < str.length(); i++)
	{
		if (str[i] == ' ') {
			str.erase(str.begin() + i);
			i--;
		}
	}
}
double calculateResult(string& postFix, map<char, double> characterMap)
{
	stack<double> operands;
	for (int i = 0; i < postFix.length(); i++)
	{
		if (postFix[i] == '+' || postFix[i] == '-' || postFix[i] == '*' || postFix[i] == '/')
		{
			double number1 = operands.top();
			operands.pop();
			double number2 = operands.top();
			operands.pop();
			if (postFix[i] == '+')
				operands.push(number1 + number2);
			else if (postFix[i] == '-')
				operands.push(number1 - number2);
			else if (postFix[i] == '*')
				operands.push(number1 * number2);
			else
				operands.push(number2 / number1);
		}
		else
		{
			operands.push(characterMap[postFix.at(i)]);
		}

	}
	return operands.top();
}
vector<string> seperateExpression(string str)
{
	vector<string> v;
	string delimiter = "=";

	size_t pos = 0;
	std::string token;
	while ((pos = str.find(delimiter)) != std::string::npos) {
		token = str.substr(0, pos);
		v.push_back(token);
		str.erase(0, pos + delimiter.length());
	}
	v.push_back(str);
	return v;
}


void createOut(double result, int i)
{
	string file_name = "Challange";
	file_name += to_string(i);
	file_name += ".out";
	ofstream outf{ file_name };

	if (!outf) {
		cerr << "result.out could not be opened for writing!" << endl;
		return;
	}

	if (i == 3)
		result = int(result);
	outf << result;
	outf.close();
}

bool isExpression(const string& strRight)
{
	for (int i = 0; i < strRight.length(); i++)
	{
		for (int j = 0; j <= 9; j++)
		{
			if (strRight[i] - '0' == j)
				return false;
		}
	}
	return true;
}

void execute()
{
	for (int i = 1; i <= 6; i++)
	{
		ifstream inf;
		string file_name = "Challange";
		file_name += to_string(i);
		file_name += ".inp";

		inf.open(file_name);
		if (!inf)
		{
			cerr << "file could not be opened for reading!" << endl;
			return;
		}

		map<char, double> operands;
		string strInput;
		while (getline(inf, strInput))
		{
			// If it finds out the keyword.
			if (strInput.find("OUT") != std::string::npos)
			{
				string output = strInput.substr(4, strInput.length());
				createOut(operands[output[0]], i);
			}
			else
			{
				//Our seperated vector includes left and right expression.
				vector<string> seperated = seperateExpression(strInput);
				if (isExpression(seperated[1]))
				{
					cleanWhiteSpaces(seperated[1]);
					string pFix = infixToPostfix(seperated[1]);
					double result = calculateResult(pFix, operands);
					string str = seperated[0];
					operands.insert({ str[0],  result });
				}
				else
				{
					string str = seperated[0];
					operands.insert({ str[0], stod(seperated[1]) });
				}
			}
		}
		inf.close();
	}
}



int main()
{
	execute();
}