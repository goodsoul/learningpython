# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

finding_nemo = media.Movie('Finding Nemo',
                           'Finding Nemo is a 2003 American computer-animated film produced by Pixar Animation Studios and released by Walt Disney Pictures.',
                           'https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg',
                           'static.hdslb.com/miniloader.swf?aid=5041925&page=1')

Atami_No_Sousakan = media.Movie('Atami No Sousakan',
                               '《热海搜查官》是由三木聡执导的电视剧，小田切让等参加演出。该剧讲述了某天，校车在接送学生的途中突然消失，连同校车一同消失的四名高中女生皆是美女，侦破此案的故事。', #NOQA
                               'https://img3.doubanio.com/view/photo/l/public/p764624925.jpg',
                               'static.hdslb.com/miniloader.swf?aid=2315366&page=1')

your_name = media.Movie('Your Name',
                  '讲述了男女高中生在梦中相遇，并寻找彼此的故事。',
                  'https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign=2a71292fc6fc1e17e9b284632bf99d66/1e30e924b899a90125d0c50f14950a7b0208f526.jpg', #NOQA
                  'static.hdslb.com/miniloader.swf?aid=13245202&page=1')
                
movie_list=[finding_nemo,Atami_No_Sousakan,your_name]

"""user fresh_tomatoes.py to build html page"""
fresh_tomatoes.open_movies_page(movie_list)


"""
#print (media.Movie.VALID_RATING)

#Print class comments
#print (media.Movie.__doc__)

#fsn.show_trailer()
#toy_story.show_trailer()
#print (toy_story.storyline)

"""                    
                        
