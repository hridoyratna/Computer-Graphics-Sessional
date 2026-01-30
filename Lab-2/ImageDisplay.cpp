#include <bits/stdc++.h>
#include<graphics.h>
using namespace std;

int main() {
    int gd, gm;
    detectgraph(&gd, &gm);
    initgraph(&gd, &gm, "BGI");
    readimagefile("download.jpg", 50, 50, 300, 300);
    outtextxy(100, 320, "Fig: Image (300x300)");
    getchar();
    return 0;
}