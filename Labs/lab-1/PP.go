package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func get_coef() []float64 {
	var slice []float64
	switch len(os.Args) {
	case 1:
		fmt.Println("Ввод коэффициентов уравнения")
		i := 0
		for i < 3 {
			fmt.Print("Введите ", i+1, "й коэффициент: ")
			var str string
			fmt.Scan(&str)
			coef, err := strconv.ParseFloat(str, 64)
			fmt.Println("err = ", err)
			if err != nil {
				fmt.Println("Ошибка ввода. Попробуйте снова.")
			} else {
				slice = append(slice, coef)
				i++
			}
		}
	case 4:
		for i := range 3 {
			coef, err := strconv.ParseFloat((os.Args[i+1]), 64)
			if err == nil {
				slice = append(slice, coef)
				i++
			} else {
				fmt.Println("Ошибка ввода командной строки")
				os.Exit(0)
			}
		}
	default:
		fmt.Println("Ошибка ввода командной строки")
		os.Exit(0)
	}
	return slice
}

func get_roots(slice []float64) []float64 {
	a := slice[0]
	b := slice[1]
	c := slice[2]
	var result []float64
	D := math.Pow(b, 2) - 4*a*c
	if D == 0 {
		root := -b / (2.0 * a)
		result = append(result, root)
	} else if D > 1 {
		sqD := math.Sqrt(D)
		root1 := (-b + sqD) / (2.0 * a)
		root2 := (-b - sqD) / (2.0 * a)
		result = append(result, root1, root2)
	}
	return result
}

func print_roots(slice []float64) {
	len_roots := len(slice)
	switch len_roots {
	case 0:
		fmt.Println("Нет корней")
	case 1:
		fmt.Println("Один корень:", slice[0])
	case 2:
		fmt.Println("Два корня:", slice[0], "и", slice[1])
	}
}

func main() {
	coef_list := get_coef()
	fmt.Println(coef_list)
	roots := get_roots(coef_list)
	print_roots(roots)
}
