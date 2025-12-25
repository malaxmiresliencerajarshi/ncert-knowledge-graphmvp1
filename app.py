import streamlit as st
import json
from streamlit_agraph import agraph, Node, Edge, Config

# 1. Setup
st.set_page_config(layout="wide", page_title="NCERT Science Graph")

# 2. Your JSON Data
# PASTE YOUR FULL JSON BETWEEN THE TRIPLE QUOTES BELOW
raw_json = '''
[
  {
    "subject": "Scientific Method",
    "relation": "is_part_of",
    "object": "Science",
    "metadata": {
      "grade": "6",
      "chapter_title": "The Wonderful World of Science",
      "importance": "core",
      "learning_outcome": "Students learn that science is a process of observation, questioning, guessing, and testing."
    },
    "context": "The scientific method is introduced in Grade 6 as the fundamental process of how science works, involving a step-by-step inquiry."
  },
  {
    "subject": "Biodiversity",
    "relation": "is_prerequisite_for",
    "object": "Ecosystem",
    "metadata": {
      "grade": "6",
      "chapter_title": "Diversity in the Living World",
      "importance": "core",
      "learning_outcome": "Understanding the variety of plants and animals in a region."
    },
    "context": "Understanding the variety of life (biodiversity) in Grade 6 is a prerequisite for studying how these organisms interact with their environment in an ecosystem in Grade 8."
  },
  {
    "subject": "Classification of Plants",
    "relation": "demonstrated_by",
    "object": "Activity: Grouping plants based on height and stem",
    "metadata": {
      "grade": "6",
      "chapter_title": "Diversity in the Living World",
      "importance": "supplementary",
      "learning_outcome": "Students learn to classify plants into herbs, shrubs, and trees by observing their physical characteristics."
    },
    "context": "Students perform a nature walk to observe and categorize plants into herbs, shrubs, and trees based on their stem and height."
  },
  {
    "subject": "Dicotyledons",
    "relation": "is_part_of",
    "object": "Classification of Plants",
    "metadata": {
      "grade": "6",
      "chapter_title": "Diversity in the Living World",
      "importance": "core",
      "learning_outcome": "Identifying plants based on the number of cotyledons in their seeds."
    },
    "context": "Dicotyledons, plants with two cotyledons, are introduced as a major group in the classification of plants, linked to taproots and reticulate venation."
  },
  {
    "subject": "Magnetic Materials",
    "relation": "is_prerequisite_for",
    "object": "Electromagnet",
    "metadata": {
      "grade": "6",
      "chapter_title": "Exploring Magnets",
      "importance": "core",
      "learning_outcome": "Distinguishing materials that are attracted to a magnet from those that are not."
    },
    "context": "The Grade 6 concept of magnetic materials like iron is necessary to understand how an iron core enhances the strength of an electromagnet in Grade 8."
  },
  {
    "subject": "Poles of Magnet",
    "relation": "extends_concept",
    "object": "Electromagnet",
    "metadata": {
      "grade": "8",
      "chapter_title": "Electricity: Magnetic and Heating Effects",
      "importance": "core",
      "learning_outcome": "Understanding that electromagnets also have North and South poles, similar to bar magnets."
    },
    "context": "Grade 8 extends the concept of magnetic poles from permanent magnets (Grade 6) to electromagnets, showing their polarity can be determined and reversed."
  },
  {
    "subject": "SI Unit of Length",
    "relation": "is_prerequisite_for",
    "object": "Measurement of Speed",
    "metadata": {
      "grade": "6",
      "chapter_title": "Measurement of Length and Motion",
      "importance": "core",
      "learning_outcome": "Understanding standard units like metre for measuring distance."
    },
    "context": "Knowledge of standard units of length (metre) from Grade 6 is a prerequisite for calculating speed (distance/time) in Grade 7."
  },
  {
    "subject": "Oscillatory Motion",
    "relation": "extends_concept",
    "object": "Simple Pendulum",
    "metadata": {
      "grade": "7",
      "chapter_title": "Measurement of Time and Motion",
      "importance": "core",
      "learning_outcome": "Applying the concept of periodic motion to measure time using a pendulum."
    },
    "context": "Grade 7 extends the concept of oscillatory motion from Grade 6 by introducing the simple pendulum and its time period for accurate time measurement."
  },
  {
    "subject": "Soluble Materials",
    "relation": "is_prerequisite_for",
    "object": "Solution",
    "metadata": {
      "grade": "6",
      "chapter_title": "Materials Around Us",
      "importance": "core",
      "learning_outcome": "Understanding that some substances dissolve in water."
    },
    "context": "The Grade 6 concept of solubility is a prerequisite for understanding solutes, solvents, and the formation of solutions in Grade 8."
  },
  {
    "subject": "Saturated Solution",
    "relation": "extends_concept",
    "object": "Solubility",
    "metadata": {
      "grade": "8",
      "chapter_title": "The Amazing World of Solutes, Solvents, and Solutions",
      "importance": "core",
      "learning_outcome": "Defining the limit of how much solute can be dissolved in a solvent at a given temperature."
    },
    "context": "Grade 8 builds on the Grade 6 concept of solubility by defining a saturated solution as the point where no more solute can be dissolved."
  },
  {
    "subject": "Temperature",
    "relation": "is_prerequisite_for",
    "object": "Heat Transfer",
    "metadata": {
      "grade": "6",
      "chapter_title": "Temperature and its Measurement",
      "importance": "core",
      "learning_outcome": "Understanding temperature as a measure of hotness or coldness."
    },
    "context": "The concept of temperature from Grade 6 is fundamental to understanding the processes of heat transfer (conduction, convection, radiation) in Grade 7."
  },
  {
    "subject": "Convection",
    "relation": "demonstrated_by",
    "object": "Activity: Heating potassium permanganate in water",
    "metadata": {
      "grade": "7",
      "chapter_title": "Heat Transfer in Nature",
      "importance": "supplementary",
      "learning_outcome": "Visualizing the movement of particles in a liquid during heating."
    },
    "context": "Students observe colored streaks of potassium permanganate rising and falling in heated water, demonstrating heat transfer through fluid motion."
  },
  {
    "subject": "Sea Breeze",
    "relation": "is_part_of",
    "object": "Convection",
    "metadata": {
      "grade": "7",
      "chapter_title": "Heat Transfer in Nature",
      "importance": "core",
      "learning_outcome": "Applying the concept of convection to a real-world atmospheric phenomenon."
    },
    "context": "Sea breeze is explained as a large-scale convection current caused by the differential heating of land and sea."
  },
  {
    "subject": "States of Water",
    "relation": "extends_concept",
    "object": "Particulate Nature of Matter",
    "metadata": {
      "grade": "8",
      "chapter_title": "Particulate Nature of Matter",
      "importance": "core",
      "learning_outcome": "Explaining solid, liquid, and gas states based on interparticle forces and spacing."
    },
    "context": "Grade 8 extends the observational understanding of water's states (Grade 6) to a scientific model based on the arrangement and forces between constituent particles."
  },
  {
    "subject": "Evaporation",
    "relation": "is_part_of",
    "object": "Water Cycle",
    "metadata": {
      "grade": "6",
      "chapter_title": "A Journey through States of Water",
      "importance": "core",
      "learning_outcome": "Understanding how liquid water turns into water vapor."
    },
    "context": "Evaporation is introduced as a key process in the water cycle, where water from oceans and lakes turns into vapor and rises into the atmosphere."
  },
  {
    "subject": "Separation of Mixtures",
    "relation": "is_prerequisite_for",
    "object": "Pure Substances",
    "metadata": {
      "grade": "6",
      "chapter_title": "Methods of Separation in Everyday Life",
      "importance": "core",
      "learning_outcome": "Learning physical methods like handpicking, sieving, and evaporation to separate components."
    },
    "context": "Understanding that mixtures can be physically separated (Grade 6) is a prerequisite for defining pure substances in Grade 8, which cannot be physically separated."
  },
  {
    "subject": "Photosynthesis",
    "relation": "extends_concept",
    "object": "Life Processes in Plants",
    "metadata": {
      "grade": "7",
      "chapter_title": "Life Processes in Plants",
      "importance": "core",
      "learning_outcome": "Identifying the inputs (CO2, water, sunlight) and outputs (glucose, oxygen) of photosynthesis."
    },
    "context": "Grade 7 details the process of photosynthesis, building upon the Grade 6 concept that plants need food to grow."
  },
  {
    "subject": "Stomata",
    "relation": "is_part_of",
    "object": "Photosynthesis",
    "metadata": {
      "grade": "7",
      "chapter_title": "Life Processes in Plants",
      "importance": "core",
      "learning_outcome": "Identifying the pores on leaves responsible for gas exchange."
    },
    "context": "Stomata are identified as the structures on leaves that allow for the exchange of carbon dioxide and oxygen, which is essential for photosynthesis."
  },
  {
    "subject": "Electric Circuit",
    "relation": "extends_concept",
    "object": "Circuit Diagram",
    "metadata": {
      "grade": "7",
      "chapter_title": "Electricity: Circuits and their Components",
      "importance": "core",
      "learning_outcome": "Learning to represent electrical components with standard symbols."
    },
    "context": "Grade 7 introduces circuit diagrams, which are symbolic representations of the simple electric circuits constructed in Grade 6."
  },
  {
    "subject": "Battery",
    "relation": "extends_concept",
    "object": "Electric Cell",
    "metadata": {
      "grade": "7",
      "chapter_title": "Electricity: Circuits and their Components",
      "importance": "core",
      "learning_outcome": "Understanding that a battery is a combination of two or more cells."
    },
    "context": "The concept of a single electric cell from Grade 6 is extended in Grade 7 to define a battery as a combination of multiple cells."
  },
  {
    "subject": "Magnetic Effect of Electric Current",
    "relation": "demonstrated_by",
    "object": "Activity: Deflection of a compass needle",
    "metadata": {
      "grade": "8",
      "chapter_title": "Electricity: Magnetic and Heating Effects",
      "importance": "core",
      "learning_outcome": "Observing that a current-carrying wire produces a magnetic field."
    },
    "context": "Students observe that a magnetic compass needle deflects when an electric current flows through a nearby wire, demonstrating the magnetic effect."
  },
  {
    "subject": "Electromagnet",
    "relation": "applied_in",
    "object": "Lifting Cranes",
    "metadata": {
      "grade": "8",
      "chapter_title": "Electricity: Magnetic and Heating Effects",
      "importance": "supplementary",
      "learning_outcome": "Understanding a large-scale industrial application of electromagnets."
    },
    "context": "The principle of the electromagnet is applied in large lifting cranes used in scrap yards to move heavy iron and steel objects."
  },
  {
    "subject": "Chemical Change",
    "relation": "is_prerequisite_for",
    "object": "Compound",
    "metadata": {
      "grade": "7",
      "chapter_title": "Changes Around Us: Physical and Chemical",
      "importance": "core",
      "learning_outcome": "Differentiating changes that form new substances from those that do not."
    },
    "context": "Understanding chemical changes (Grade 7) is essential to grasp how elements combine to form compounds with new properties in Grade 8."
  },
  {
    "subject": "Neutralisation Reaction",
    "relation": "applied_in",
    "object": "Ant Bite Treatment",
    "metadata": {
      "grade": "7",
      "chapter_title": "Exploring Substances: Acidic, Basic, and Neutral",
      "importance": "supplementary",
      "learning_outcome": "Applying the concept of acid-base neutralisation to a daily life problem."
    },
    "context": "The sting of an ant, which is acidic (formic acid), can be relieved by applying a basic substance like baking soda, demonstrating neutralisation."
  },
  {
    "subject": "Force",
    "relation": "extends_concept",
    "object": "Pressure",
    "metadata": {
      "grade": "8",
      "chapter_title": "Pressure, Winds, Storms, and Cyclones",
      "importance": "core",
      "learning_outcome": "Understanding pressure as force applied per unit area."
    },
    "context": "Grade 8 extends the concept of force (a push or pull) from Grade 7 by introducing pressure, which depends on both the force and the area over which it acts."
  },
  {
    "subject": "Atmospheric Pressure",
    "relation": "is_prerequisite_for",
    "object": "Wind Formation",
    "metadata": {
      "grade": "8",
      "chapter_title": "Pressure, Winds, Storms, and Cyclones",
      "importance": "core",
      "learning_outcome": "Understanding that the air around us exerts pressure."
    },
    "context": "The concept of atmospheric pressure is a prerequisite for understanding that differences in air pressure cause air to move, resulting in wind."
  },
  {
    "subject": "Reflection of Light",
    "relation": "extends_concept",
    "object": "Spherical Mirrors",
    "metadata": {
      "grade": "8",
      "chapter_title": "Light: Mirrors and Lenses",
      "importance": "core",
      "learning_outcome": "Applying laws of reflection to understand image formation by curved surfaces."
    },
    "context": "Grade 8 extends the laws of reflection learned with plane mirrors in Grade 7 to explain how spherical mirrors form different types of images."
  },
  {
    "subject": "Convex Mirror",
    "relation": "applied_in",
    "object": "Vehicle Side-view Mirrors",
    "metadata": {
      "grade": "8",
      "chapter_title": "Light: Mirrors and Lenses",
      "importance": "core",
      "learning_outcome": "Understanding the practical use of convex mirrors for a wider field of view."
    },
    "context": "Convex mirrors are used as side-view mirrors in vehicles because they provide a wider view of the road behind, even though they form diminished images."
  },
  {
    "subject": "Lens",
    "relation": "demonstrated_by",
    "object": "Activity: Water drop on an oiled surface",
    "metadata": {
      "grade": "8",
      "chapter_title": "Light: Mirrors and Lenses",
      "importance": "supplementary",
      "learning_outcome": "Observing the magnifying effect of a curved transparent surface."
    },
    "context": "Students observe that a drop of water on an oiled glass strip acts like a simple lens, magnifying the text placed underneath it."
  },
  {
    "subject": "Reproduction",
    "relation": "is_part_of",
    "object": "Life Processes",
    "metadata": {
      "grade": "6",
      "chapter_title": "Living Creatures: Exploring their Characteristics",
      "importance": "core",
      "learning_outcome": "Understanding that living beings produce new ones of their own kind."
    },
    "context": "Reproduction is introduced in Grade 6 as one of the essential characteristics that differentiate living beings from non-living things."
  },
  {
    "subject": "Sexual Reproduction",
    "relation": "extends_concept",
    "object": "Reproduction",
    "metadata": {
      "grade": "8",
      "chapter_title": "Our Home: Earth, a Unique Life Sustaining Planet",
      "importance": "core",
      "learning_outcome": "Understanding the role of two parents and gametes in producing offspring with variations."
    },
    "context": "Grade 8 expands on the general concept of reproduction from Grade 6 by detailing sexual reproduction, involving male and female gametes."
  },
  {
    "subject": "Pollination",
    "relation": "is_part_of",
    "object": "Sexual Reproduction in Plants",
    "metadata": {
      "grade": "8",
      "chapter_title": "Our Home: Earth, a Unique Life Sustaining Planet",
      "importance": "core",
      "learning_outcome": "Understanding the transfer of pollen as a key step in plant reproduction."
    },
    "context": "Pollination is explained as the process where pollen is transferred from the male part to the female part of a flower, leading to fertilization."
  },
  {
    "subject": "Ecosystem",
    "relation": "extends_concept",
    "object": "Habitat",
    "metadata": {
      "grade": "8",
      "chapter_title": "How Nature Works in Harmony",
      "importance": "core",
      "learning_outcome": "Understanding the interaction between living (biotic) and non-living (abiotic) components."
    },
    "context": "Grade 8 builds upon the Grade 6 concept of a habitat (a place where an organism lives) by defining an ecosystem as the complex interaction of all biotic and abiotic factors in that area."
  },
  {
    "subject": "Food Chain",
    "relation": "is_part_of",
    "object": "Ecosystem",
    "metadata": {
      "grade": "8",
      "chapter_title": "How Nature Works in Harmony",
      "importance": "core",
      "learning_outcome": "Tracing the flow of energy from producers to consumers in an ecosystem."
    },
    "context": "A food chain is introduced as a simple linear pathway showing the feeding relationships and energy flow within an ecosystem."
  },
  {
    "subject": "Rotation of Earth",
    "relation": "is_prerequisite_for",
    "object": "Phases of the Moon",
    "metadata": {
      "grade": "7",
      "chapter_title": "Earth, Moon, and the Sun",
      "importance": "core",
      "learning_outcome": "Understanding that Earth's rotation causes the day-night cycle."
    },
    "context": "Understanding Earth's daily rotation (Grade 7) is necessary to comprehend why the Moon's position in the sky changes daily, which is linked to observing its phases (Grade 8)."
  },
  {
    "subject": "Phases of the Moon",
    "relation": "demonstrated_by",
    "object": "Activity: Ball and stick model with a light source",
    "metadata": {
      "grade": "8",
      "chapter_title": "Keeping Time with the Skies",
      "importance": "supplementary",
      "learning_outcome": "Simulating how the illuminated portion of the Moon visible from Earth changes as it revolves."
    },
    "context": "A student holding a ball (Moon) and turning around in front of a light source (Sun) simulates how different phases of the Moon are observed from Earth."
  },
  {
    "subject": "Solar Calendar",
    "relation": "extends_concept",
    "object": "Revolution of the Earth",
    "metadata": {
      "grade": "8",
      "chapter_title": "Keeping Time with the Skies",
      "importance": "core",
      "learning_outcome": "Connecting the concept of a year to Earth's revolution around the Sun."
    },
    "context": "Grade 8 explains that solar calendars are based on the time it takes for the Earth to complete one revolution around the Sun, a concept introduced in Grade 7."
  },
  {
    "subject": "Cell",
    "relation": "demonstrated_by",
    "object": "Activity: Observing onion peel under a microscope",
    "metadata": {
      "grade": "8",
      "chapter_title": "The Invisible Living World: Beyond Our Naked Eye",
      "importance": "core",
      "learning_outcome": "Visualizing the basic structural unit of a plant."
    },
    "context": "Students prepare a slide of onion peel to observe the rectangular, brick-like arrangement of plant cells under a microscope."
  },
  {
    "subject": "Cell Wall",
    "relation": "is_part_of",
    "object": "Plant Cell",
    "metadata": {
      "grade": "8",
      "chapter_title": "The Invisible Living World: Beyond Our Naked Eye",
      "importance": "core",
      "learning_outcome": "Identifying the rigid outer layer that provides structure to plant cells."
    },
    "context": "The cell wall is identified as a key feature of plant cells, distinguishing them from animal cells and providing structural support."
  }
]'''

# 3. Logic
data = json.loads(raw_json)
nodes = []
edges = []
nodes_added = set()

# Color mapping for the "Magic" look
colors = {"6": "#FFD700", "7": "#FF8C00", "8": "#FF4500"}

for item in data:
    grade = item["metadata"]["grade"]
    curr_color = colors.get(grade, "#6495ED")
    
    if item["subject"] not in nodes_added:
        nodes.append(Node(id=item["subject"], label=item["subject"], size=20, color=curr_color))
        nodes_added.add(item["subject"])
    
    if item["object"] not in nodes_added:
        # We might not know the grade of the object yet, so we use a default
        nodes.append(Node(id=item["object"], label=item["object"], size=20, color="#999999"))
        nodes_added.add(item["object"])
        
    edges.append(Edge(source=item["subject"], target=item["object"], label=item["relation"]))

# 4. Display
st.title("🎓 NCERT Science Knowledge Map")
st.write("Visualizing connections between the Science concepts of Grade 7, and 8.")

config = Config(width=1000, height=700, directed=True, physics=True)
return_value = agraph(nodes=nodes, edges=edges, config=config)

# Show details when a node is clicked
if return_value:
    st.sidebar.header("Concept Details")
    for item in data:
        if item["subject"] == return_value:
            st.sidebar.info(f"**Concept:** {item['subject']}")
            st.sidebar.write(f"**Context:** {item['context']}")

            st.sidebar.write(f"**Chapter:** {item['metadata']['chapter_title']}")
