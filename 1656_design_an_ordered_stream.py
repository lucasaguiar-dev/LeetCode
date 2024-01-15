class OrderedStream {
    arrayPrimario:string[]
    ponteiro:number
    constructor(n: number) {
        this.arrayPrimario = new Array(n).fill('')
        this.ponteiro = 0
    }
    insert(idKey: number, value: string): string[] {
        this.arrayPrimario[idKey-1] = value
        const arrayValue:string[] = []
        for (let i = this.ponteiro; i<this.arrayPrimario.length; i++){
            if (this.arrayPrimario[i]===''){
                this.ponteiro = i
                break
            }
            arrayValue.push(this.arrayPrimario[i])
        }
        return arrayValue
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */
