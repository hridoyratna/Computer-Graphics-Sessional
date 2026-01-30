#include <bits/stdc++.h>
#include<graphics.h>
using namespace std;

int main() {
    int gd, gm;
    detectgraph(&gd, &gm);
    initgraph(&gd, &gm, "BGI");
    setcolor(CYAN);
    rectangle(80, 80, 180, 180);
    rectangle(120, 120, 220, 220);
    line(80, 180, 120, 220);
    line(80, 80, 120, 120);
    line(180, 180, 220, 220);
    line(180, 80, 220, 120);
    outtextxy(140, 240, "Fig: Cube");
    getchar();
    return 0;
}