% Facts about diseases and dietary recommendations
diet_recommendation(diabetes, 'Limit sugar intake and consume complex carbohydrates.').
diet_recommendation(hypertension, 'Reduce salt intake and eat potassium-rich foods.').
diet_recommendation(cholesterol, 'Consume foods low in saturated and trans fats.').
diet_recommendation(celiac, 'Avoid gluten-containing foods like wheat, barley, and rye.').
diet_recommendation(anemia, 'Eat iron-rich foods like lean meats, beans, and leafy greens.').
diet_recommendation(gout, 'Limit foods high in purines like red meat and alcohol.').

% Predicate to suggest a diet based on disease
suggest_diet(Disease, Recommendation) :-
    diet_recommendation(Disease, Recommendation),
    write('For '), write(Disease), write(' disease: '), write(Recommendation), nl.

%?- suggest_diet(diabetes, Recommendation).