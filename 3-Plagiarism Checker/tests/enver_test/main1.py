#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>

void yazdir_cikis(double res, int i, bool isIntChallenge);
std::queue<std::string> ayirici(std::string s);
bool birifadeVarmi(std::string sagTaraf);
std::string yenihalecevir(std::string s);
int oncelik(char isaret);
double hesaplayici(std::map<char, double> myOperands, std::string yenihal);

int main()
{

	// 6 tane challenge'� oku
	for (int i = 1; i <= 6; i++)
	{
		bool isIntChallenge = true;
		std::ifstream myFile;
		std::string dosyaAdi = "Challange";
		dosyaAdi += std::to_string(i);
		dosyaAdi += ".inp";
		myFile.open(dosyaAdi);
		std::map<char, double> myOperands;
		if (myFile)
		{
			std::string str;
			while (std::getline(myFile, str))
			{
				//If it finds '.'
				if (str.find(".") != std::string::npos)
					isIntChallenge = false;
				//There is out
				if (str.find("OUT") != std::string::npos)
				{
					std::string out = str.substr(4, str.length());
					std::cout << "What is my out: " << out << '\n';
					yazdir_cikis(myOperands[out[0]], i, isIntChallenge);
				}
				else
				{
					std::queue<std::string> ayrilmis = ayirici(str);
					std::string sol = ayrilmis.front();
					ayrilmis.pop();
					std::string sag = ayrilmis.front();
					ayrilmis.pop();
					// sa� taraf bir expression ise
					if (birifadeVarmi(sag))
					{
						//bu ifadedeki bo�luklar� temizlemeliyiz.
						for (int i = 0; i < sag.length(); i++)
						{
							if (sag[i] == ' ')
							{
								sag.erase(sag.begin() + i);
								i--;
							}
						}
						//bosluklari temizledikten sonra
						//postfix d�n���m� yapaca��z.
						//postfix olay�n� youtube ve geeksforgeeksten ara�t�rarak bulup, ��rendim.
						//matematiksel i�lemler algoritmalarla nas�l yap�l�r �eklinde ara�t�rmalar yapt�m.
						std::string yenihal = yenihalecevir(sag);
						double sonucum = hesaplayici(myOperands, yenihal);
						if (isIntChallenge)
							myOperands.insert({ sol[0], (int)sonucum });
						else
							myOperands.insert({ sol[0], sonucum });
					}
					// sa� taraf bir atama i�eriyorsa
					else
					{
						if (isIntChallenge)
							myOperands.insert({ sol[0], stoi(sag) });
						else
							myOperands.insert({ sol[0], stod(sag) });
					}
				}
			}
		}
		else
		{
			std::cout << "File could not be opened" << std::endl;
		}
		myFile.close();
	}
}

double hesaplayici(std::map<char, double> myOperands, std::string yenihal)
{
	std::stack<double> operands;
	for (int i = 0; i < yenihal.length(); i++)
	{
		if (yenihal[i] == '+' || yenihal[i] == '-' || yenihal[i] == '*' || yenihal[i] == '/')
		{
			double number1 = operands.top();
			operands.pop();
			double number2 = operands.top();
			operands.pop();
			if (yenihal[i] == '+')
				operands.push(number1 + number2);
			else if (yenihal[i] == '-')
				operands.push(number1 - number2);
			else if (yenihal[i] == '*')
				operands.push(number1 * number2);
			else
				operands.push(number2 / number1);
		}
		else
		{
			operands.push(myOperands[yenihal.at(i)]);
		}
	}
	return operands.top();
}

int oncelik(char isaret)
{
	if (isaret == '^')
		return 3;
	else if (isaret == '*' || isaret == '/')
		return 2;
	else if (isaret == '+' || isaret == '-')
		return 1;
	else
		return -1;
}

std::string yenihalecevir(std::string s)
{
	std::stack<char> st;
	st.push('N');
	int l = s.length();
	std::string ns;
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

		else
		{
			while (st.top() != 'N' && oncelik(s[i]) <=
				oncelik(st.top()))
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

bool birifadeVarmi(std::string sagTaraf)
{
	for (auto ch : sagTaraf)
	{
		if (ch == '+' || ch == '-' || ch == '*' || ch == '/')
			return true;
	}
	return false;
}

std::queue<std::string> ayirici(std::string s)
{
	std::queue<std::string> ayir;
	std::string delim = "=";

	size_t pos = 0;
	std::string token;
	while ((pos = s.find(delim)) != std::string::npos)
	{
		token = s.substr(0, pos);
		ayir.push(token);
		s.erase(0, pos + delim.length());
	}
	ayir.push(s);
	return ayir;
}

void yazdir_cikis(double res, int i, bool isIntChallenge)
{
	//if (isIntChallenge)
	//	res = int(res);
	
	std::cout << "What is my result: " << res << '\n';
	std::ofstream out;
	std::string dosyaAdi = "Challange";
	dosyaAdi += std::to_string(i);
	dosyaAdi += ".out";
	out.open(dosyaAdi);
	if (out)
	{
		out << res;
		out.close();
	}
	else
	{
		std::cout << "File could not be created to write" << std::endl;
	}
	out.close();
}