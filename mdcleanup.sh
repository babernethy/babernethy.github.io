for file in *.md; docd 
    sed -i '' '/^layout:/d' "$file"
done
