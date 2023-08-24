const{Worker,
    isMainThread, 
    parentPort, 
    workerData
} = require('worker_threads');

function gerarNumeroAleatorio(){
    return Math.floor(Math.random() * 5) + 1;
}

function esperar(ms){
    return new Promise(function(resolve){
        setTimeout(resolve,ms);
    })
}

async function realizarCorrida(idDaThread){
    let posicaoAtual = 0;
    let totalPassos = 0;

    console.log(`Thread ${idDaThread} - Iniciando`);
    
    while(posicaoAtual < 50 ){
        const passos = gerarNumeroAleatorio();
        totalPassos += passos;
        posicaoAtual +=passos;

        console.log(`Vez da Thread ${idDaThread}`);
        console.log(`Número sorteado ${passos}`);
        console.log(`Thread ${idDaThread} Andou ${passos} casas`);
        console.log(`Posição atual da Thread  ${idDaThread}: ${posicaoAtual}`);

        await esperar(1000);

    }

    console.log(`Thread ${idDaThread} - Chegou à posição 50! Total de passos: ${totalPassos}`);

    return totalPassos;
    
}

if(isMainThread) {
    const numThreads = 2;
    let threadsFinalizadas = 0;
    const resultados = [];

    async function iniciarCorrida(){
        const promessas = [];

        for(let i = 1; i<= numThreads;i++){
            const thread = new Worker(__filename, {
                workerData: i
            });
            
            thread.on('exit',() =>{
                console.log(`Thread secundária ${i}finalizada.`);
                threadsFinalizadas++;

                if(threadsFinalizadas === numThreads){
                    const indiceVencedor = resultados.findIndex((passos,indice) => indice === 0 || passos < resultados[indiceVencedor]);
                    const idDaThreadVencedora = indiceVencedor + 1;
                    console.log(`A Thread ${idDaThreadVencedora} venceu com ${resultados[indiceVencedor]} passos!`);
                }
            });
            
            promessas.push(new Promise((resolve, reject)=>{
                thread.on('message',resolve);
                thread.on('error',reject);
            }));
        }
        resultados.push(...await Promise.all(promessas));
    }
    iniciarCorrida();
} else{
    async function threadSecundaria(){
        const idDaThread = workerData !== undefined ? 'Thread'+workerData : 'desconhecida';

        const totalPassos = await realizarCorrida(idDaThread);


        parentPort.postMessage(totalPassos);

    }
    threadSecundaria();
}