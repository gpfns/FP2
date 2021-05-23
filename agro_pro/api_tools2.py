def fun_market_price_data():
    l1 = ['Rice', 'Wheat', 'Atta(Wheat)', 'Gram Dal', 'Tur / Arhar Dal', 'Urad Dal', 'Moong Dal', 'Masoor Dal',
          'Sugar', 'Milk', 'Groundnut Oil(Packed)', 'Mustard Oil(Packed)', 'Vanaspati(Packed)', 'Soya Oil(Packed)',
          'Sunflower Oil(Packed)', 'Palm Oil(Packed)', 'Gur', 'Tea Loose', 'Salt Pack(Iodised)', 'Potato', 'Onion',
          'Tomato']


def api_h_crop_prediction_b(l1, l2, ph, rf, land):
    return """<html>
      <body>
      <h3> Optimal Crop to Grow is <b> {0} </b> </h3>
      <h3> Estimated Profit is : {1}   </h3>
      <h2> Government Minimum Support Price is Available @ {2}/quintal </h2>
      <br>
      </body>""".format("Wheat", "62000", "7300")


def api_h_crop_prediction_a(l1, l2, ph, rf, land, nitro, pho, pot):
    return """<html>
      <body>
      <h3> Optimal Crop to Grow is <b> {0} </b> </h3>
      <h3> Estimated Profit is : {1}   </h3>
      <h2> Government Minimum Support Price is Available @ {2}/quintal </h2>
      <br>
      </body>""".format("Wheat", "62000", "7300")
