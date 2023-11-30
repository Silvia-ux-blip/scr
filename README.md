# scr
# Descorchando la Excelencia
# Un Viaje Analítico para Prever la Calidad de Vinos Blancos
## Datos del vino

Es un estudio sobre el vinho verde , un producto único de la región de Minho (noroeste) de Portugal. De contenido medio alcohólico, es especialmente apreciado por su frescor (especialmente en verano). Este vino representa el 15% de la producción total portuguesa, y alrededor del 10% se exporta, principalmente vino blanco.

En los últimos años, el interés por el vino ha aumentado, lo que ha llevado al crecimiento de la industria vitivinícola. Como consecuencia, las empresas están invirtiendo en nuevas tecnologías para mejorar la producción y venta de vino. La certificación de calidad es un paso crucial para ambos procesos y actualmente depende en gran medida de la cata del vino por parte de expertos humanos. 
* Este trabajo tiene como objetivo la predicción de las preferencias de vino a partir de pruebas analíticas objetivas que están disponibles en la etapa de certificación.

La certificación del vino se evalúa generalmente mediante pruebas fisicoquímicas y sensoriales. Las pruebas fisicoquímicas de laboratorio que se utilizan habitualmente para caracterizar el vino incluyen la determinación de los valores de densidad, alcohol o pH, mientras que las pruebas sensoriales se basan principalmente en expertos humanos.

Presento un estudio de caso para modelar preferencias gustativas basadas en datos analíticos que, están fácilmente disponibles en el paso de certificación del vino. Construir un modelo de este tipo es valioso no sólo para las entidades de certificación sino también para los productores de vino e incluso para los consumidores. Puede utilizarse para apoyar las evaluaciones de vinos del enólogo, mejorando potencialmente la calidad y la rapidez de sus decisiones. Además, medir el impacto de las pruebas fisicoquímicas en la calidad final del vino es útil para mejorar el proceso de producción. Además, puede ayudar en el marketing objetivo, es decir, aplicando técnicas similares para modelar las preferencias del consumidor en nichos de mercado y/o mercados rentables.

## Conjunto de datos sobre la calidad del vino

El conjunto de datos sobre calidad del vino implica predecir la calidad de los vinos blancos en una escala dada  con las medidas químicas de cada vino. https://archive.ics.uci.edu/dataset/186/wine+quality

Producido exclusivamente en la región demarcada de Vinho Verde en el noroeste de Portugal, sólo se produce a partir de las variedades de uva autóctonas de la región, como Alvarinho, Loureiro y Trajadura, conservando su tipicidad de aromas y sabores como única en el mundo del vino. Este dataset contiene un total de 4898 muestras blancas.

Cita para usar los datos
P. Cortez, A. Cerdeira, F. Almeida, T. Matos y J. Reis. Modelado de preferencias de vino mediante extracción de datos a partir de propiedades fisicoquímicas. En Sistemas de apoyo a la decisión, Elsevier, 47(4):547-553, 2009.

Las variables que figuran en el DataSet son:

**Acidez fija.**

La mayoría de los ácidos involucrados fijos o no volátiles (no se evaporan fácilmente) es la suma de todos aquellos ácidos que, cuando el vino es sometido a calor, no se evaporarán. 
A este grupo pertenecen los ácidos tartárico, málico, láctico y cítrico. Su presencia se nota de forma característica a través del paladar. El más importante de todos ellos es el ácido tartárico, de ahí que la medición de la acidez fija se haga en gramos de éste por litro. Gracias a los ácidos que conforman la acidez fija se preservan las cualidades naturales del vino, así como el color. 

**Acidez volátil.**

Es aquella que se desprenderá del vino al calentarlo,  generalmente se nota en forma característica a través de la nariz. 
Se produce durante la fermentación alcohólica, no es posible fabricar vino sin generar algo de ácido acético. La cantidad de ácido acético en el vino, en niveles demasiado altos puede provocar un sabor desagradable a vinagre. 

**Ácido cítrico.**

Se encuentra en pequeñas cantidades, puede añadir "frescura" y sabor a los vinos. En ciertas circunstancias, los enólogos pueden optar por ajustar la acidez del vino agregando ácido cítrico. Este ajuste se realiza con el objetivo de equilibrar la acidez y mejorar el perfil sensorial del vino.

**Azúcar residual.**

La cantidad de azúcares residuales en el vino influirá en su dulzura percibida. Los vinos secos tienen bajos niveles de azúcares residuales, mientras que los vinos dulces tienen cantidades más altas. Es lo que queda después de que las uvas hayan pasado por el proceso de elaboración del vino. Las uvas contienen azúcares de frutas (fructosa y glucosa) y el residual es lo que queda después de que la levadura haya masticado esos azúcares.

**Cloruros.**

La cantidad de sal en el vino. Los componentes minerales que encontramos en la uva proceden directamente del suelo, el cual se verá afectado por los abonos y tratamientos fitosanitarios. En una botella de vino hay unos 3 gramos de estos compuestos del vino, que le proporcionan un cierto sabor salado. También potencian otros sabores y dan un cierto cuerpo.

**Dióxido de azufre libre.**

Es un óxido con una avalada trayectoria de uso en el consumo humano. Utilizado en este terreno en forma de sal (Metabisulfito de Potasio), este componente se oxida ante los fenoles presentes en el vino, consumiendo el oxígeno presente y generando tres compuestos químicos que, en conjunto, son conocidos como sulfitos. El libre es más importante desde el punto de vista funcional, ya que es la forma activa que realiza las funciones protectoras.

**Dióxido de azufre total.**

Permite evitar la proliferación de microorganismos habituales tanto en la uva como en el mosto, fundamental para evitar la modificación del color propio de un vino. Es importante controlar y medir los niveles de dióxido de azufre en el vino para garantizar su estabilidad y calidad, pero también porque el SO2 en exceso puede afectar negativamente al sabor y aroma del vino, así como tener implicaciones para la salud en algunas personas sensibles al azufre. Los enólogos suelen seguir pautas y regulaciones específicas con respecto a los niveles de SO2 en el vino.

**Densidad.**

El primero y más importante es el agua. Grosso modo, si un vino tiene un 13 % de alcohol, el 87 % restante es agua. En estos dos líquidos están disueltos el resto de los componentes. El alcohol etílico es el segundo compuesto mayoritario y proviene de la fermentación del azúcar por las levaduras.

**PH.**

El pH, junto con el azúcar, es una de las medidas clave para determinar el inicio de la vendimia. Este parámetro es importante para conocer la evolución de los componentes ácidos presentes en el vino, que tienen un papel clave en todo el proceso de elaboración del producto final. Influyen en el sabor, aroma y color del vino.

**Sulfatos.**

Los sulfitos son unos de los antioxidantes más utilizados en la industria del vino para prevenir la oxidación, resultado de la exposición a la luz y que puede causar efectos indeseados como sabores y colores extraños. También tiene propiedades antisépticas y desinfectantes e impide el deterioro del vino provocado por actividades microbianas.

**Alcohol.**

Sin duda, el contenido de alcohol es un valor fundamental para un vino y es uno de los más importantes parámetros de calidad y valoración. Se mide la cantidad de alcohol etílico o etanol que hay en 100 ml de vino y suele expresarse en porcentaje (% vol.). El etanol es el soporte básico de los aromas de los vinos. 
Según la normativa vigente al respecto, el grado alcohólico es una indicación obligatoria en el etiquetado del vino.

**Calidad (puntuación entre 0 y 10).**

La calidad del vino es un concepto subjetivo y puede evaluarse en función de varios aspectos, como el sabor, el aroma, el equilibrio, la complejidad y la estructura. No hay una clasificación universalmente aceptada de la calidad del vino en una escala del 1 al 9.
1. **1-3: Deficiente o Pobre:** Vinos que tienen defectos notables, como sabores desequilibrados, aromas desagradables o fallos en la estructura. Pueden carecer de complejidad y presentar signos de deterioro.

2. **4-6: Aceptable o Medio:** Vinos que son satisfactorios pero pueden tener áreas donde podrían mejorar. Pueden tener algunos rasgos positivos, pero también pueden mostrar ciertos defectos menores.

3. **7-9: Bueno a Excelente:** Vinos de alta calidad. En este rango, puedes encontrar vinos bien equilibrados, con sabores y aromas agradables, complejidad y una estructura sólida. Los vinos en la parte superior de esta escala (8-9) son generalmente considerados excepcionales, con características distintivas y gran longevidad.

Además de se tiene que considerar la evaluación de una serie de propiedades organolépticas que contribuyen a sus características generales.

**Taninos:**
   - Los taninos son compuestos que provienen de las pieles, semillas y tallos de las uvas, así como del envejecimiento en barricas de roble. Contribuyen a la estructura, el color y la sensación astringente del vino, especialmente en los vinos tintos.

**Color:**
   - El color del vino, particularmente en los vinos tintos, se evalúa en términos de intensidad, tonalidad y claridad. Los pigmentos responsables del color son los antocianos en los tintos y los flavonoles en los blancos.

**Aromas y Sabores:**
   - La evaluación sensorial de aromas y sabores es fundamental. Los compuestos volátiles, como los ésteres y terpenos, contribuyen a los perfiles aromáticos, mientras que las notas de frutas, flores, especias, hierbas y otros elementos son esenciales para la apreciación del sabor.

**Cuerpo:**
   - La sensación de cuerpo en boca está relacionada con la combinación de alcohol, azúcares y otros componentes. Los vinos se describen comúnmente como ligeros, medianos o corpulentos.

**Persistencia:**
   - La persistencia o longitud del sabor es la duración de los sabores en boca después de tragar el vino. Un vino con buena persistencia se considera más complejo y satisfactorio.

**Estructura:**
   - La estructura del vino se refiere a cómo interactúan los componentes individuales, como la acidez, los taninos y el alcohol, para formar un todo armonioso. Un buen equilibrio y estructura proporcionan una experiencia de degustación más completa.
