from alayout import *

with LinearLayout(layout_width='fill_parent', layout_height='fill_parent', orientation='vertical'):
	with TextView(id='@+id/text', layout_width='wrap_content', layout_height='wrap_content') as tv:
		tv['text'] = 'Hello, I am a TextView'
	Button(
			id='@+id/button', layout_width='wrap_content', layout_height='wrap_content',
			text='Hello, I am a Button'
		)

"""
Original example XML from the documentation:

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
              android:layout_width="fill_parent" 
              android:layout_height="fill_parent" 
              android:orientation="vertical" >
    <TextView android:id="@+id/text"
              android:layout_width="wrap_content"
              android:layout_height="wrap_content"
              android:text="Hello, I am a TextView" />
    <Button android:id="@+id/button"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Hello, I am a Button" />
</LinearLayout>
"""
