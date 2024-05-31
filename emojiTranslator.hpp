#ifndef EMOJITRANSLATOR_HPP
#define EMOJITRANSLATOR_HPP

#include <pybind11/pybind11.h>
#include <map>
#include <string>
using namespace std;

static map<string, string> EMOJIS_MAP = {
    {":football:" , u8"\U0001F3C8"},
    {":angry:" , u8"\U0001F620"},
    {":ant:" , u8"\U0001F41C"},
    {":eyes:" , u8"\U0001F440"},
    {":lips:" , u8"\U0001F444"},
    {":rose:" , u8"\U0001F339"},
    {":pizza:" , u8"\U0001F355"},
    {":smile:" , u8"\U0001F604"},
    {":smirk:" , u8"\U0001F60F"},
    {":tulip:" , u8"\U0001F337"},
    {":violin:" , u8"\U0001F3BB"},
    {":watch:" , u8"\U0000231A"},
    {":ocean:" , u8"\U0001F30A"},
    {":moon:" , u8"\U0001F314"},
    {":wheelchair:" , u8"\U0000267F"},
    {":wineGlass:" , u8"\U0001F377"},
    {":boot:" , u8"\U0001F462"},
    {":womens:" , u8"\U0001F6BA"},
    {":world_map:" , u8"\U0001F5FA"},
    {":gift:" , u8"\U0001F381"}
};  

string translator(string str);

namespace py = pybind11;

PYBIND11_MODULE(emojiTranslator_pythonBinding, mod) {
    mod.def("emojiTrans", &translator, "Translate text to emojis.");
}

#endif
