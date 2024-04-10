#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main()
{
    string nome, sobrenome;
    cout << "Nome: ";
    cin >> nome;

    cout << "Sobrenome: ";
    cin >> sobrenome;

    char ultima = nome[nome.length() -1];

    cout << sobrenome << " , " << nome[0] << " " << ultima << endl;

    return 0;

}