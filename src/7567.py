def main():
    plates = input()

    result = 10

    rev = plates[0]

    for plate in plates[1:]:
        if rev == plate:
            result += 5
        else:
            result += 10
        
        rev = plate
    
    print(result)

if __name__ == "__main__":
    main()