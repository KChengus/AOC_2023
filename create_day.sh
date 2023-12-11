
#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

map="Day$1"

if [ -d "$map" ]; then
    echo "Map exits. Exiting"
    exit 0
fi 

p1="p1.py"
p2="p2.py"

mkdir "$map"
cp "skeleton.py" "$map/$map$p1"
cp "skeleton.py" "$map/$map$p2"
cd "$map"
touch "testp1.txt" "testp2.txt" "input.txt"

echo "Created $map"