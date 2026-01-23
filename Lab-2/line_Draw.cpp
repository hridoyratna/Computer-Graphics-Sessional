#include <iostream>
#include<stdio.h>
#include<graphics.h>

using namespace std;

int main()
{
    int gd,gm;
    detectgraph(&gd,&gm);
    initgraph(&gd,&gm,"c:\\TURBOC3\\BGI");

    line(20,30,40,50);
    getchar ();
    return 0;
}