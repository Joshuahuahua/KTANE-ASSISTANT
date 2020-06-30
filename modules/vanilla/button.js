var _pj;
function _pj_snippets(container) {
    function in_es6(left, right) {
        if (((right instanceof Array) || ((typeof right) === "string"))) {
            return (right.indexOf(left) > (- 1));
        } else {
            if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                return right.has(left);
            } else {
                return (left in right);
            }
        }
    }
    container["in_es6"] = in_es6;
    return container;
}
_pj = {};
_pj_snippets(_pj);
function button(bomb_data, button_word, button_colour) {
    var button_raw;
    button_raw = [button_colour, button_word];
    if ((((button_raw === ["red", "hold"]) || ((button_word === "detonate") && (bomb_data["bat_total"] > 1))) || (_pj.in_es6("FRK", bomb_data["ind_LIT"]) && (bomb_data["bat_total"] > 2)))) {
        return "Press";
    } else {
        return "Hold";
    }
}
function button2(stripe) {
    if ((stripe === "blue")) {
        return 4;
    } else {
        if ((stripe === "yellow")) {
            return 5;
        } else {
            return 1;
        }
    }
}

//# sourceMappingURL=button.js.map
