#include "emojiTranslator.hpp"

string translator(string str) {
    int index = 0;
    int size = str.size();
    for (int i = 1; i < size; i++) {
        if (str[i] == *L":") {
            if(i!=0 && str[i-1]=='\\'){
                return "Not Found!";
            }else {
                if (i - index==1) {
                    return "Not Found!";
                }
                map<string, string>::iterator itr;
                itr = EMOJIS_MAP.find(str.substr(index, i - index + 1));
                if (itr == EMOJIS_MAP.end()) {
                    return "Not Found!";
                }
                string temp = itr->second;
                str.replace(index, i - index + 1 , temp);
                int tempIndex = i - index + 1 - temp.size();
                size -= tempIndex;
                i -= tempIndex;
                index = -1;
            }
        }
    }
    return str;
}

