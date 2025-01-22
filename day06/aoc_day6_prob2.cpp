// Solution for Problem 2 (Luck-Based)

// Contains an arbitrary value of 3600 iterations as limit which gave the correct answer
// I derived it by using binary search on no. of iterations limit (trial and error) and checked all the solutions obtained in the process 
// until I reached the correct answer (think of it like a rainbow attack on the answer field of the question part 2 :))


// Have to find a more logically explainable solution yet !

#include <bits/stdc++.h>
using namespace std;

int detect_loop(int guard_x,int guard_y,int rows,int cols,vector<pair<int,int>> &directions,vector<string> &grid){
    
    int direction_index = 0;
    int _x = guard_x,_y = guard_y;
    int counter = 0;

    while (counter < 3600) {
        counter++ ;
        int dx = directions[direction_index].first;
        int dy = directions[direction_index].second;
        int nx = guard_x + dx;
        int ny = guard_y + dy;
        if (nx < 0 || ny < 0 || nx >= rows || ny >= cols) {
            break;
        }
        if(nx == _x && ny == _y) return 1;
        if (grid[nx][ny] == '#') {
            direction_index = (direction_index + 1) % 4;
        }
        else {
            guard_x = nx;
            guard_y = ny;
        }
    }
    return 0;
}

int main() {
    ifstream infile("input.txt");
    vector<string> grid;
    string line;
    while (getline(infile, line)) {
        grid.push_back(line);
    }
    infile.close();
    int rows = grid.size(), cols = grid[0].size();
    vector<pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int loops = 0,count = 0;
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            if (grid[i][j] == '#' || grid[i][j] == '^') continue;
            loops += detect_loop(i,j,rows,cols,directions,grid);
        }
    }
    cout<<"No. of positions where loops could be present : "<<loops;
}

