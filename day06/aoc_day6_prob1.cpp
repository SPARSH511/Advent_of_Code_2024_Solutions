// Brute Force Solution for Problem 1

#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream infile("input.txt");
    vector<string> grid;
    string line;
    while (getline(infile, line)) {
        grid.push_back(line);
    }
    infile.close();
    int rows = grid.size(), cols = grid[0].size();
    int guard_x = 0, guard_y = 0, direction_index = 0;
    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] == '^') {
                guard_x = r;
                guard_y = c;
                break;
            }
        }
    }
    vector<pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    set<pair<int, int>> visited;
    visited.insert({guard_x, guard_y});
    while (true) {
        int dx = directions[direction_index].first;
        int dy = directions[direction_index].second;
        int nx = guard_x + dx;
        int ny = guard_y + dy;
        if (nx < 0 || ny < 0 || nx >= rows || ny >= cols) {
            break;
        }
        if (grid[nx][ny] == '#') {
            direction_index = (direction_index + 1) % 4;
        } else {
            guard_x = nx;
            guard_y = ny;
            visited.insert({guard_x, guard_y});
            grid[guard_x][guard_y] = 'x';
        }
    }
    cout << "Distinct positions visited: " << visited.size() << endl;

    cout<< "\nThe map of places visited (marked x): \n";
    for(auto row: grid){
        for(auto c: row){
            cout<<c;
        }
        cout<<"\n";
    }
    return 0;
}
