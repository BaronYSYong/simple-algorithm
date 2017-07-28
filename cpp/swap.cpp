/*!
 * @file  swap.cpp
 * @brief swap without temp
 * @date 2017/07/28
 * @author YoonSeong Yong 
 * 
 */


#include <iostream>

void swap1(float &x, float &y){
    x = x + y;
    y = x - y;
    x = x - y;
}

void swap2(float &x, float &y){
    x = x * y;
    y = x / y;
    x = x / y;
}

//~ void swap3(float &x, float &y){
    //~ x = x ^ y;
    //~ y = x ^ y;
    //~ x = x ^ y;
//~ }

int main(){
    float a = 3.142, b = 9.1244;
    
    std::cout << "Before swap" << std::endl;
    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;   
     
    swap2(a,b);
    
    std::cout << "After swap" << std::endl;
    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;
}
