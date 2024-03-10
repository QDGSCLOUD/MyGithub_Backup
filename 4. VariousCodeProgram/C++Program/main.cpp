#include <iostream>
using namespace std;

int cnt = 0;

class Sheep
{
public:
    char name[10];
    int age;
    static  int cnt;    // 声明静态成员变量,   但是静态成员变量不是类的成员变量, 只是写在类里面
                              //  作用域是 类里面 和 类的所有的对象


    static int sheep_num()
    {
        return cnt ;   // 访问静态成员变量.
    }

    Sheep()
    {
        cnt ++ ;  // 每次访问构造函数的时候, cnt 都要 加 一
    }

    ~Sheep()
    {
        cnt --;
    }



private:

};

// 定义类里面声明的静态成员边浪
int Sheep::cnt = 0 ;      // 如果直接写 int Sheep::cnt;  也是默认的 0


int main(){
    Sheep *p = new Sheep[10];

    // 在实际中推荐用下面两种方式访问静态成员变量和静态成员函数.
    cout << Sheep::cnt << endl;           // 访问静态成员变量
    cout << Sheep::sheep_num() << endl;    // 访问静态成员函数


    return 0;
}