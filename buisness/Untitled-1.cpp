// Path: source/contest/2019-2020/1/1

int main () {
    int n;
    cin >> n;
    int a[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    int max = a[0];
    int min = a[0];
    for (int i=0; i<n; i++) {
        if (a[i] > max) {
            max = a[i];
        }
        if (a[i] < min) {
            min = a[i];
        }
    }
    cout << max << " " << min << endl;
    return 0;
}

// 1.2
// Language: cpp
// Path: source/contest/2019-2020/1/2

int main () {
    int n;
    cin >> n;
    int a[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    
    int max = a[0];
    int min = a[0];
    int maxIndex = 0;
    int minIndex = 0;
    for (int i=0; i<n; i++) {
        if (a[i] > max) {
            max = a[i];
            maxIndex = i;
        }
        if (a[i] < min) {
            min = a[i];
            minIndex = i;
        }
    }
    
    int sum = 0;
    if (maxIndex > minIndex) {
        for (int i=minIndex+1; i<maxIndex; i++) {
            sum += a[i];
        }
    } else {
        for (int i=maxIndex+1; i<minIndex; i++) {
            sum += a[i];
        }
    }
    
    cout << sum << endl;
    return 0;
}

// 1.3
// Language: cpp
// Path: source/contest/2019-2020/1/3

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.4
// Language: cpp
// Path: source/contest/2019-2020/1/4

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.5
// Language: cpp
// Path: source/contest/2019-2020/1/5

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.6
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.7
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.8
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.9
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.10
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.11
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.12
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.13
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.14
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.15
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.16
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

// 1.17
// Language: cpp

int main () {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    int c[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
    }
    for (int i=0; i<n; i++) {
        cin >> b[i];
    }
    for (int i=0; i<n; i++) {
        cin >> c[i];
    }
    
    int sum = 0;
    for (int i=0; i<n; i++) {
        sum += a[i] * b[i] * c[i];
    }
    
    cout << sum << endl;
    return 0;
}

<<<<<<print>>>>>>cash-flow for more content follow task.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb

__cpp_capture_star_this = 0; function() {delta' (primary' (type.src'codeName))} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb follow'-supra'(tern'ex'cell'ent) {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb

__cpp_capture_star_this = 0; function() {delta' (primary' (type.src'codeName))} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb follow'-supra'(tern'ex'cell'ent) {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb
{(type.src'codeName)} {type.src'codeName} = {t = more.content_flow_type @executive projection for canvas type.01" ~}{~}expression disturb